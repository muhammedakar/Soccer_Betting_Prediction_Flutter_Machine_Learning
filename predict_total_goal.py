
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import numpy as np
import pandas as pd
from lib import encoding as en, outliers as out
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from lightgbm import LGBMRegressor

pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.max_column', None)
pd.set_option('display.width', 500)

df = pd.read_csv('dataset/iddiaa.csv')

df[['Referee']] = (
    en.rare_encoder(df[['Referee']], 0.02))

df_final = df[
    ['Week', 'Home', 'Away', 'Referee', 'Home_Value', 'Away_Value', 'Home_Atk', 'Home_Ort', 'Home_Def', 'Home_Gen',
     'Away_Atk', 'Away_Ort', 'Away_Def', 'Away_Gen', 'Home_Bet', 'Draw_Bet', 'Away_Bet', 'Total_Goal', 'Alt_Bet',
     'Ust_Bet', 'Home_Point', 'Away_Point']]

result = out.grab_col_names(df_final)
cat_cols, num_cols = result[0], result[1]

df_final = en.one_hot_encoder(df_final, ['Home', 'Away', 'Referee'], drop_first=True)

# rs = StandardScaler()
# l = [col for col in df_final.columns if col not in ['Total_Goal']]
# df_final[l] = rs.fit_transform(df_final[l])

df_final['Total_Goal'].std()

X = df_final.drop(['Total_Goal'], axis=1)
y = df_final['Total_Goal']

X.columns


def base_models(X, y):
    print("Base Models....")
    classifiers = [('LR', LinearRegression()),
                   ('KNN', KNeighborsRegressor()),
                   ("CART", DecisionTreeRegressor()),
                   ("RF", RandomForestRegressor()),
                   ('GBM', GradientBoostingRegressor()),
                   ('XGBoost', XGBRegressor(use_label_encoder=False, eval_metric='logloss')),
                   ('LightGBM', LGBMRegressor()),
                   ('CatBoost', CatBoostRegressor(verbose=False))
                   ]
    score = pd.DataFrame(index=['rmse', 'r2_score'])
    for name, classifier in classifiers:
        rmse = np.mean(np.sqrt(-cross_val_score(classifier, X, y, cv=3, scoring="neg_mean_squared_error")))
        r2 = np.mean(cross_val_score(classifier, X, y, cv=3, scoring="r2"))
        score[name] = [rmse, r2]
        print(f'{name} hesaplandı...')
    print(score.T)


base_models(X, y)

rf_params = {"max_depth": [5, 8, 15, None],
             "max_features": [5, 7, "auto"],
             "min_samples_split": [8, 15, 20],
             "n_estimators": [200, 500]}

gbm_params = {"learning_rate": [0.01, 0.1],
              "max_depth": [3, 8],
              "n_estimators": [500, 1000],
              "subsample": [1, 0.5, 0.7]}

lightgbm_params = {"learning_rate": [0.01, 0.1],
                   "n_estimators": [300, 500],
                   "colsample_bytree": [0.7, 1]}

catboost_params = {"iterations": [200, 500],
                   "learning_rate": [0.01, 0.1],
                   "depth": [3, 6]}

classifiers = [("RF", RandomForestRegressor(), rf_params),
               ('GBM', GradientBoostingRegressor(), gbm_params),
               ('LightGBM', LGBMRegressor(), lightgbm_params),
               ("CatBoost", CatBoostRegressor(), catboost_params)]


def hyperparameter_optimization(X, y, cv=3):
    print("Hyperparameter Optimization....")
    best_models = {}
    score = pd.DataFrame(index=['rmse', 'r2_score'])
    for name, classifier, params in classifiers:
        gs_best = GridSearchCV(classifier, params, cv=cv, n_jobs=-1, verbose=False).fit(X, y)
        final_model = classifier.set_params(**gs_best.best_params_)
        rmse = np.mean(np.sqrt(-cross_val_score(classifier, X, y, cv=3, scoring="neg_mean_squared_error")))
        r2 = np.mean(cross_val_score(classifier, X, y, cv=3, scoring="r2"))
        score[name] = [rmse, r2]
        print(f'{name} hesaplandı...')
        best_models[name] = final_model
    print(score.T)
    return best_models

hyperparameter_optimization(X, y)

cb_reg = CatBoostRegressor().fit(X, y)
joblib.dump(cb_reg, "deployment/bet_total_goal.pkl")


def plot_importance(model, features, num=len(X), save=False):
    feature_imp = pd.DataFrame({'Value': model.feature_importances_, 'Feature': features.columns})
    plt.figure(figsize=(10, 10))
    sns.set(font_scale=1)
    sns.barplot(x="Value", y="Feature", data=feature_imp.sort_values(by="Value",
                                                                     ascending=False)[0:num])
    plt.title('Features')
    plt.tight_layout()
    plt.show()
    if save:
        plt.savefig('importances.png')


plot_importance(cb_reg, X)