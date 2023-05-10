import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import xgboost as xgb
import pickle
import os
import warnings
warnings.filterwarnings('ignore')


def get_recommendation(model, scaler, le, data):
    data = np.array(data)
    data = data.reshape(1, -1)
    data = scaler.transform(data)
    prob = model.predict_proba(data)
    prob = prob.reshape(-1)
    label_order = le.classes_
    recommendation = list(zip(label_order, prob))
    recommendation.sort(key=lambda x:-x[1])
    return recommendation[:5]

path = os.getcwd()
model_path = path + '\group5\model.bin'
scaler_path = path + '\group5\scaler.pkl'
encoder_path = path + '\group5\encoder.pkl'

model = xgb.XGBClassifier()
model.load_model(model_path)

with open(scaler_path, 'rb') as f:
    sc = pickle.load(f)

with open(encoder_path, 'rb') as f:
    le = pickle.load(f)

ans = get_recommendation(model, sc, le, [1, 2, 0, 3, 20000])
print(ans)