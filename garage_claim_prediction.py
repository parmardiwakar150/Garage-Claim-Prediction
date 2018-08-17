import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline

data_feb = pd.read_excel('Mplus Claim FEB-2018.xlsx')
data_mar = pd.read_excel('Mplus Claim MAR-18.xlsx')
data_jan = pd.read_excel('Claims JAN-2018.xlsx')
data_dec = pd.read_excel('Claim DEC-2017.xlsx')
data_nov = pd.read_excel('Claims NOV-2017.xlsx')
data_oct = pd.read_excel('claims OCT-2017.xlsx')

df = data_feb[['PartID', 'SubPartID','PartTypeID', 'ModelID', 'EstimatePartRate', 'EstimateRRAmt', 'EstimateDentingAmt', 'EstimatePaintingAmt', 'GarageID', 'GarageStateID', 'GarageCityID', 'ClaimRefNo']]
dm = data_mar[['PartID', 'SubPartID','PartTypeID', 'ModelID', 'EstimatePartRate', 'EstimateRRAmt', 'EstimateDentingAmt', 'EstimatePaintingAmt', 'GarageID', 'GarageStateID', 'GarageCityID', 'ClaimRefNo']]
dj = data_jan[['PartID', 'SubPartID','PartTypeID', 'ModelID', 'EstimatePartRate', 'EstimateRRAmt', 'EstimateDentingAmt', 'EstimatePaintingAmt', 'GarageID', 'GarageStateID', 'GarageCityID', 'ClaimRefNo']]
dd = data_dec[['PartID', 'SubPartID','PartTypeID', 'ModelID', 'EstimatePartRate', 'EstimateRRAmt', 'EstimateDentingAmt', 'EstimatePaintingAmt', 'GarageID', 'GarageStateID', 'GarageCityID', 'ClaimRefNo']]
dn = data_nov[['PartID', 'SubPartID','PartTypeID', 'ModelID', 'EstimatePartRate', 'EstimateRRAmt', 'EstimateDentingAmt', 'EstimatePaintingAmt', 'GarageID', 'GarageStateID', 'GarageCityID', 'ClaimRefNo']]
do = data_oct[['PartID', 'SubPartID','PartTypeID', 'ModelID', 'EstimatePartRate', 'EstimateRRAmt', 'EstimateDentingAmt', 'EstimatePaintingAmt', 'GarageID', 'GarageStateID', 'GarageCityID', 'ClaimRefNo']]


data = df.append(dm).append(dj).append(dd).append(dn).append(do)

data = data[pd.isna(data.ModelID) == False]
data = data.fillna(data.mean())
data['TotalClaimAmt'] = data.EstimateDentingAmt + data.EstimatePaintingAmt + data.EstimatePartRate + data.EstimateRRAmt


X = data[['PartID', 'SubPartID', 'PartTypeID', 'ModelID', 'GarageID', 'GarageStateID', 'GarageCityID']]
y = data.TotalClaimAmt

X.PartID = X.PartID.astype('category')
X.SubPartID = X.SubPartID.astype('category')
X.PartTypeID = X.PartTypeID.astype('category')
X.ModelID = X.ModelID.astype('category')
X.GarageID = X.GarageID.astype('category')
X.GarageStateID = X.GarageStateID.astype('category')
X.GarageCityID = X.GarageCityID.astype('category')

from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
X = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1)

from sklearn.tree import DecisionTreeRegressor
from lightgbm import LGBMRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import BaggingRegressor

tree_model = DecisionTreeRegressor(criterion='mae')
lgb_model = LGBMRegressor(n_estimators=10000)
forest_model = RandomForestRegressor(n_estimators=100)
bag_model = BaggingRegressor(n_estimators=100,n_jobs= -1)

tree_model.fit(X_train,y_train)
#lgb_model.fit(X_train, y_train)
#forest_model.fit(X_train, y_train)
#bag_model.fit(X_train, y_train)

prediction = tree_model.predict(X_test)
from sklearn.metrics import mean_squared_error , accuracy_score
mean_squared_error(y_test,prediction)

len(y_test[((y_test - prediction) / y_test * 100) < 1]) / len(y_test)