# -*- coding: utf-8 -*-

from flask import Flask, request,  render_template
import model
app = Flask(__name__)
@app.route("/testing", methods =["POST","GET"])
def testing():
    predict_real = ""
    confid = ""
    datetime = ""
    sensor1_PM2 = ""
    sensor2_PM2 = ""
    temperature = ""
    relative_humidity = ""
    
    if request.method == "POST":
        datetime = request.form["datetime"]
        sensor1_PM2 = request.form["sensor1_PM2"]
        sensor2_PM2 = request.form["sensor2_PM2"]
        temperature = request.form["temperature"]
        relative_humidity = request.form["relative_humidity"]
        
        predict_real, confid = model.predict(datetime, sensor1_PM2, sensor2_PM2,
                                             temperature, relative_humidity)

    return render_template("testing.html",target = predict_real, confidence = confid)

@app.route("/")
def Index():
   return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True,use_reloader=False)
