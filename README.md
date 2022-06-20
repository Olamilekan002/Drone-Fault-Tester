# Umoja-Hack-Africa-2022 🥇

### UmojaHack Africa 2022 #3: Faulty Air Quality Sensor Brief Description.

The objective of this challenge is to create a classification model to identify a device has an off set fault or not, regardless of the device. The model can be used by AirQo to automatically flag a device that is returning faulty data. 

Have a look on [Zindi](https://zindi.africa/competitions/umojahack-africa-2022-beginner-challenge).

### Approach ⏬
* Import all necessary Libraries
* Load Data (Test and Train)
* EDA
* Feature Engineering
* Modelling
* Deployment

#### Load Data 📉
The train contain 293563 records of time series data and 7 fields, dated from 2021 - 2022.

* The missing values were filled using forward fill approach because it is a time series data.
* Outliers were replaced with mean in some features.

#### Featuring Engineering ☸️
* Date diff was extracted
* Day, month and hour of report was extracted
* More features were generated from other features

#### Model 🚀
The base model was RandomForest with an accuracy of 93% using stratifiedKFold for data splitting. Other models include:
* Catboost: Accuracy 96%
* LightGBM: Accuracy 94%
* Xgboost: Accuracy 93%

#### Deployment ✈️
The model was deployed to Heroku using flask and other necessary libraries.

[link]()
