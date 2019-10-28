
# # libraries and links


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import math
import datetime
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
import statsmodels.api as sm
from scipy import stats
from statsmodels.compat import lzip
import statsmodels
from statsmodels.stats.outliers_influence import variance_inflation_factor
from pandas.plotting import register_matplotlib_converters
from sklearn.linear_model import LassoCV, LassoLarsCV, LassoLarsIC
import time
from sklearn.preprocessing import PolynomialFeatures




sold=pd.read_csv("flatten_sold.csv")


# # create new columns




sold["sale_price_raw_log"]=np.log(sold["sale_price_raw"])
sold["price_listed_raw_log"]=np.log(sold["price_listed_raw"])
sold["days_on_market2"]=np.absolute(sold["days_on_market"])
sold["days_on_market3"]=sold["days_on_market2"].fillna(0)
sold["sale_price_raw_m"]=round((sold["sale_price_raw"])/1000000,3)
sold["price_listed_raw_m"]=round((sold["price_listed_raw"])/1000000,3)
sold["building_type_n"], uniques = pd.factorize(sold["building_type"])
sold["hood_n"], uniques = pd.factorize(sold["hood"])
sold['sale_date2'] = pd.to_datetime(sold['sale_date'])
sold['month'] = pd.DatetimeIndex(sold['sale_date2']).month
sold['day'] = pd.DatetimeIndex(sold['sale_date2']).day
sold["bedrooms_n"], uniques = pd.factorize(sold["bedrooms"])
sold["bathrooms_n"], uniques = pd.factorize(sold["bathrooms"])
# sold['year'] = pd.DatetimeIndex(sold['sale_date2']).year


print(sold.dtypes)
print(sold.isnull().sum())
sold.describe()
sold.head()
sold.columns


# # create addt'l dataframes

sold2=sold[["bedrooms","bathrooms","sqft_raw","ppsqft_raw","sale_price_raw_log","price_listed_raw_log","building_type","hood"]]
sold3=sold[["bedrooms","bathrooms","sqft_raw","ppsqft_raw","sale_price_raw_m","price_listed_raw_m","building_type","hood"]]


# # groupby



sold.groupby("building_type").size()
print("Apartments sold: " + str((sold.groupby("hood").size().sort_values(ascending=False)).head(20)))
(sold3[sold3["building_type"]=="condo"].groupby("hood").mean().sort_values("sale_price_raw_m",ascending=False)).head()
(sold3[sold3["building_type"]=="co-op"].groupby("hood").mean().sort_values("sale_price_raw_m",ascending=False)).head()
(sold3[sold3["building_type"]=="condo"].groupby("hood").agg(['count', 'sum', 'min', 'max', 'mean', 'std'])['sale_price_raw_m'].sort_values("mean",ascending=False)).head(10)
(sold3[sold3["building_type"]=="co-op"].groupby("hood").agg(['count', 'sum', 'min', 'max', 'mean', 'std'])['sale_price_raw_m'].sort_values("mean",ascending=False)).head(10)


h=(sold.groupby("hood").agg({"sale_price_raw_m":["mean"],"price_listed_raw_m":["mean"]}))
h.columns = ["_".join(x) for x in h.columns.ravel()]
h.sort_values("sale_price_raw_m_mean",ascending=False).head(10)


# # visual

sns.set(style="whitegrid")
sns.set(font_scale=2)
g = sns.catplot(x="building_type", y="sale_price_raw_m", hue="month", data=sold,
                height=11, kind="bar", palette="muted")
g.despine(left=True)
g.set_ylabels("sale price in millions")
g.set_xlabels("building type")


sns.set(style="whitegrid")
sns.set(font_scale=2)
g = sns.catplot(x="building_type", y="sale_price_raw_m", hue="month", data=sold,
                height=11, kind="bar", palette="muted")
g.despine(left=True)
g.set_ylabels("sale price in millions")
g.set_xlabels("building type")



f, ax = plt.subplots(figsize=(15, 9))
sns.set(font_scale=2)
g=sns.lineplot(x="sale_date2", y="sale_price_raw", data=sold)
ax.set(xlabel='sale date', ylabel='sale price')



f, ax = plt.subplots(figsize=(9, 9))
sns.lineplot(x="sale_date2", y="price_listed_raw", data=sold)
ax.set(xlabel='sale date', ylabel='list price')




sns.jointplot(x='price_listed_raw',y='sqft_raw',data=sold,kind='reg')


sns.jointplot(x='sale_price_raw_log',y='sqft_raw',data=sold,kind='reg')


sns.distplot(sold["days_on_market3"])


sns.jointplot(x='sale_price_raw_log',y='days_on_market3',data=sold,kind='reg')


sns.set(style="ticks")
sns.set(font_scale=2)
f, ax = plt.subplots(figsize=(18, 18))
ax.set_xscale("log")
my_order = sold.groupby(["hood"])["sale_price_raw_m"].median().sort_values(ascending=False).head(10).index
sns.boxplot(x="sale_price_raw_m", y="hood", data=sold,
            whis="range", palette="vlag",order=my_order)
ax.xaxis.grid(True)
ax.set(xlabel="mean sale price in millions")
sns.despine(trim=True, left=True)


sns.set(style="ticks")
sns.set(font_scale=2)
f, ax = plt.subplots(figsize=(18, 18))
ax.set_xscale("log")
my_order = sold.groupby(["hood"])["price_listed_raw_m"].median().sort_values(ascending=False).head(10).index
sns.boxplot(x="price_listed_raw_m", y="hood", data=sold,
            whis="range", palette="vlag",order=my_order)
ax.xaxis.grid(True)
ax.set(xlabel="mean listing price in millions")
sns.despine(trim=True, left=True)



sns.pairplot(sold2,hue="building_type",palette='coolwarm')



g = sns.FacetGrid(sold2, col="building_type")
g = g.map(plt.hist, "sale_price_raw_log")


# # Prediction

sold_prediction=sold[["history_id","building_id","bedrooms_n","bathrooms_n","sqft_raw","sale_price_raw_m","price_listed_raw_m","building_type_n","hood_n","month","day"]]



sold_prediction["sqft_raw"]=sold_prediction["sqft_raw"].fillna(sold_prediction['sqft_raw'].mean())
sold_prediction["price_listed_raw_m"]=sold_prediction["price_listed_raw_m"].fillna(sold_prediction['price_listed_raw_m'].mean())


print(sold_prediction.isnull().sum())

sold_prediction.columns


# ### Standard Errors assume that the covariance matrix of the errors is correctly specified


# lm = smf.ols(formula='sale_price_raw_m ~ history_id + building_id + bedrooms_n + bathrooms_n + sqft_raw + price_listed_raw_m + building_type_n + hood_n + month + day', data=sold_prediction).fit()
# history_id and day shoots VIF...
lm = smf.ols(formula='sale_price_raw_m ~ price_listed_raw_m + building_id  + bedrooms_n + bathrooms_n + sqft_raw  + building_type_n + hood_n + month + day', data=sold_prediction).fit()
print(lm.summary())


# ### heteroscedasticity robust (HC0)


lm2 = smf.ols(formula='sale_price_raw_m ~ price_listed_raw_m + building_id  + bedrooms_n + bathrooms_n + sqft_raw  + building_type_n + hood_n + month + day', data=sold_prediction).fit(cov_type='HC0')
print(lm2.summary())


# ### residual plot


pred_val = lm2.fittedvalues.copy()
true_val = (sold_prediction['sale_price_raw_m']).values.copy()
residual = true_val - pred_val

fig, ax = plt.subplots(figsize=(6,2.5))
_ = ax.scatter(residual, pred_val)


residual.sum()

# ### RMSE

def rmse_accuracy_percentage(a,b): 
    print("RMSE is:",np.round(np.sqrt(sum(((np.array(a)-np.array(b))**2))/len(a)),2))
rmse_accuracy_percentage(true_val,pred_val)
print("stdev: ", str(np.std(sold_prediction["sale_price_raw_m"])))


# print(lm2.summary().as_latex())

# for table in lm2.summary().tables:
#     print(table.as_latex_tabular())




# ### Assumption of Multicollinearity



# Assumption of Multicollinearity

variables = lm2.model.exog
vif = [variance_inflation_factor(variables, i) for i in range(variables.shape[1])]
vif 


np.array(vif).mean()


# ### correlation


sold_prediction.corr()


# correlation 
al_cor=sold_prediction.corr()
al_cor=al_cor.unstack()
al_cor["sale_price_raw_m"].sort_values(ascending=False)



# Assumption of Independent Errors

statsmodels.stats.stattools.durbin_watson(lm2.resid)



name = ['Jarque-Bera', 'Chi^2 two-tail prob.', 'Skew', 'Kurtosis']
test = sms.jarque_bera(lm2.resid)
print(lzip(name, test))


# Assumption of Normality of the Residuals

sold_prediction['sale_price_raw_m'].plot(kind='hist', 
                       title= 'Log of Sale Price Distribution')



# Assumption of Normality of the Residuals

sold_prediction['sale_price_raw_m_log'] = np.log(sold_prediction['sale_price_raw_m'])
sold_prediction['sale_price_raw_m_log'].plot(kind='hist', 
                       title= 'Log of Sale Price Distribution')


# Assumption of Normality of the Residuals

stats.probplot(lm2.resid, dist="norm", plot= plt)
plt.title("Model1 Residuals Q-Q Plot")


# Assumption of Homoscedasticity

name = ['Lagrange multiplier statistic', 'p-value', 
        'f-value', 'f p-value']
test = sms.het_breuschpagan(lm2.resid, lm2.model.exog)
lzip(name, test)

