from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np


def lReg_predict(X, y, new_data):
    lReg = LinearRegression().fit(X, y)
    new_data = pd.DataFrame(new_data)
    predict = lReg.predict(new_data)
    y_pred = lReg.predict(X)
    mse = mean_squared_error(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    rmse = np.sqrt(mse)
    r_score = lReg.score(X,y)
    print(f'MSE:{mse}\nRMSE:{rmse}\nMAE:{mae}\nR-KARE:{r_score}')
    print(f'Bağımlı değişken ortalaması:{y.mean()[0]}\nStandart sapması:{y.std()[0]}')
    return predict
