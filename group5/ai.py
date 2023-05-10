import datetime
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import xgboost as xgb
import pickle
import warnings
warnings.filterwarnings('ignore')


def get_recommendation(category, data):
    model_path = 'aimodels/'+category+'_model.bin'
    scaler_path = 'aimodels/'+category+'_sc.pkl'
    encoder_path = 'aimodels/'+category+'_le.pkl'
    model = xgb.XGBClassifier()
    model.load_model(model_path)

    with open(scaler_path, 'rb') as f:
        scaler = pickle.load(f)

    with open(encoder_path, 'rb') as f:
        encoder = pickle.load(f)

    data = np.array(data)
    data = data.reshape(1, -1)
    data = scaler.transform(data)
    prob = model.predict_proba(data)
    prob = prob.reshape(-1)
    label_order = encoder.classes_
    recommendation = list(zip(label_order, prob))
    recommendation.sort(key=lambda x:-x[1])
    return recommendation[:5]

def get_day(input_date): # '2023-05-12' 형식
    date_info = input_date.split('-')
    date_info = [int(x) for x in date_info]
    dt = datetime.date(date_info[0], date_info[1], date_info[2])
    day = dt.weekday()
    if day < 4:
        return 0
    elif day == 4:
        return 1
    else:
        return 2
    
def get_bungi(input_date): # '2023-05-12' 형식
    date_info = input_date.split('-')
    date_info = [int(x) for x in date_info]
    if date_info[1] < 4:
        return 1
    elif 4 <= date_info[1] < 7:
        return 2
    elif 7 <= date_info[1] < 10:
        return 3
    else:
        return 4
    
def get_time(input_time): # '09:50'형식
    time_info = input_time.split(':')
    if int(time_info[0]) < 17:
        return 0
    else:
        return 1