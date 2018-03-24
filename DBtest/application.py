from flask import Flask, request, redirect, url_for, make_response, render_template


application = Flask(__name__)

words = []


@application.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        color = request.form['color']
        lat = request.form['lat']
        lon = request.form['lon']
        desc = request.form['desc']
        time = request.form['time']
        info = ",".join([color,lat,lon,desc,time])
        with open('events.csv','a') as events:
            events.write(info + "\n")
        print(info)
    return render_template('index.html')


if __name__ == '__main__':
    application.run(debug=True)
