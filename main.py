import pandas as pd
from lib import outliers as out, encoding as en, summary as sum
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression as lr
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.max_column', None)
pd.set_option('display.width', 500)

df = pd.read_csv('dataset/iddiaa.csv')


result = out.grab_col_names(df)

cat_cols, num_cols, cat_but_car = result[0], result[1], result[2]

sum.cat_summary(df, cat_but_car)

df.head()

for col in num_cols:
    sum.target_summary_with_num(df, 'Ust', col)


df[['Referee']] = (
    en.rare_encoder(df[['Referee']], 0.02))

df_final = df[
    ['Week', 'Home', 'Away', 'Referee', 'Home_Value', 'Away_Value', 'Home_Atk', 'Home_Ort', 'Home_Def', 'Home_Gen',
     'Away_Atk', 'Away_Ort', 'Away_Def', 'Away_Gen', 'Home_Bet', 'Draw_Bet', 'Away_Bet', 'Target']]

df_final = en.one_hot_encoder(df_final, ['Home', 'Away', 'Referee'], drop_first=True)

X = df_final.drop(['Target'], axis=1)
y = df_final['Target']

df_final.head()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=45)

########################################################################
# Logistic Regression
########################################################################

reg_model = lr(multi_class='ovr').fit(X_train, y_train)

y_pred = reg_model.predict(X_test)
print(classification_report(y_test, y_pred))

########################################################################
# Random Forest Classifier
########################################################################

ran_model = RandomForestClassifier().fit(X_train, y_train)

y_pred = ran_model.predict(X_test)
print(classification_report(y_test, y_pred))

########################################################################
# Catboost Classifier
########################################################################

catb_model = CatBoostClassifier().fit(X_train, y_train)

y_pred = catb_model.predict(X_test)
print(classification_report(y_test, y_pred))


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


plot_importance(catb_model, X)

joblib.dump(catb_model, "deployment/bet_predict.pkl")

########################################################################
# XGB Classifier
########################################################################

xgb_model = XGBClassifier().fit(X_train, y_train)

y_pred = xgb_model.predict(X_test)
print(classification_report(y_test, y_pred))
