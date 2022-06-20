import pandas as pd
#import numpy as np
#import pickle
import joblib
print("pass")

def load_model():
    model = joblib.load('saved_model.sav')
    #model = pickle.load(open("saved_model.sav", 'rb'))
    return model

def date_preprocessing(data):
    # get a days difference from a given date
    data['datediff'] = (pd.to_datetime("2022-03-19 11:01:18.751351") - pd.to_datetime(data['Datetime'])).dt.days
    
    # Extract day, month and year from the Datetime column
    data['Datetime_day'] = pd.to_datetime(data['Datetime']).dt.day
    data['Datetime_month'] = pd.to_datetime(data['Datetime']).dt.month
    data['Datetime_hour'] = pd.to_datetime(data['Datetime']).dt.hour
    
    return data
    
def feat_generation(data):
    #feature generation
    
    data['sensorcombo'] = (data['Sensor1_PM2.5'] + data['Sensor2_PM2.5'])/2
    data['diffsensor'] = (data['Sensor1_PM2.5'] - data['Sensor2_PM2.5'])

    data['temp/hum'] = data['Relative_Humidity']/data['Temperature']
    
    return data

def preprocessing(data):
    #processing date column and also generating new features
    data = date_preprocessing(data)

    #generating features from sensor
    data = feat_generation(data)

    print("pass2")
    X = data[['Temperature', 'Relative_Humidity', 'datediff','diffsensor',
       'sensorcombo', 'Datetime_day', 'Datetime_month', 'temp/hum',
       'Datetime_hour']]
    return X


def predict(Datetime, Sensor1_PM2, Sensor2_PM2, Temperature, Relative_Humidity):
    
    X_dataframe = pd.DataFrame([{'Datetime':Datetime, 'Sensor1_PM2.5':int(Sensor1_PM2), 'Sensor2_PM2.5':int(Sensor2_PM2),
                                 'Temperature':int(Temperature),'Relative_Humidity':int(Relative_Humidity)}])
    #print(X_dataframe)
    
    preprocessed_test_data = preprocessing(X_dataframe)
    
    prediction,confid = makePrediction(preprocessed_test_data)
    print("SUCCESS2")
    return prediction,confid 

def makePrediction(test_pre):
    classifier = load_model()
    
    predict_val = 0
    confidence = 0
    predict_val = classifier.predict(test_pre)
    confidence = classifier.predict_proba(test_pre)[:,1][0].round(2)
    confidence*=100
    
    if predict_val == 1:
        predict_real = "The Drone is Faulty"
    else:
        predict_real = "The Drone is Not Faulty"
        
    return predict_real, confidence

#print(predict('2021-11-03 04:06:31','50','39','34','50'))
# -*- coding: utf-8 -*-

