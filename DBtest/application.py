from flask import Flask, request, redirect, url_for, make_response, render_template
import json
import pandas


application = Flask(__name__)

dataDF = pandas.DataFrame(columns=["color","lat","lon","desc","date"])
with open('events.csv','r') as events:
    dataDF=pandas.read_csv(events)


@application.route('/', methods=['GET', 'POST'])
def form_data():
    global dataDF
    if request.method == 'POST':
        color = request.form['color']
        lat = request.form['lat']
        lon = request.form['lon']
        desc = request.form['desc']
        date = request.form['date']

        tmp_dict = {"color":color,"lat":lat,"lon":lon,"desc":desc,"date":date}
        tmp_arr = [tmp_dict]
        tempDF = pandas.DataFrame(tmp_arr)
        dataDF = pandas.concat([dataDF, tempDF])
        print(dataDF)

        #write tp scv to save
        info = ",".join([color,lat,lon,desc,date])
        with open('events.csv','a') as events:
            events.write(info + "\n")
        #print(info)

    return render_template('index.html')

@application.route('/textpass', methods=['GET', 'POST'])
def text_pass():
    global dataDF
    dataDF = dataDF[['color','lat','lon','desc','date']]
    return render_template('textpass.html', data=dataDF.to_json(orient='split'))

@application.route('/displaypage', methods=['GET', 'POST'])
def display_page():
    global dataDF
    dataDF = dataDF[['color', 'lat', 'lon', 'desc', 'date']]
    return render_template('DisplayPage.html', data=dataDF.to_json(orient='split'))

@application.route('/displaypagegradient', methods=['GET', 'POST'])
def display_page_gradient():
    global dataDF
    dataDF = dataDF[['color', 'lat', 'lon', 'desc', 'date']]
    return render_template('DisplayPageGradient.html', data=dataDF.to_json(orient='split'))

@application.route('/final', methods=['GET', 'POST'])
def display_final():
    global dataDF
    dataDF = dataDF[['color', 'lat', 'lon', 'desc', 'date']]
    if request.method == 'POST':
        color = request.form['color']
        lat = request.form['lat']
        lon = request.form['lon']
        desc = request.form['desc']
        date = request.form['date']

        tmp_dict = {"color":color,"lat":lat,"lon":lon,"desc":desc,"date":date}
        tmp_arr = [tmp_dict]
        tempDF = pandas.DataFrame(tmp_arr)
        dataDF = pandas.concat([dataDF, tempDF])
        print(dataDF)

        #write tp scv to save
        info = ",".join([color,lat,lon,desc,date])
        with open('events.csv','a') as events:
            events.write(info + "\n")
        #print(info)
    return render_template('dot/dot_two.html', data=dataDF.to_json(orient='split'))

@application.route('/index2', methods=['GET', 'POST'])
def display_index2():
    global dataDF
    dataDF = dataDF[['color', 'lat', 'lon', 'desc', 'date']]
    return render_template('index2.html', data=dataDF.to_json(orient='split'))

if __name__ == '__main__':
    application.run(debug=True)
