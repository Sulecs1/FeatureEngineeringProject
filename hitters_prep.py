"""
Değişkenleri anlamak için öncelikle baseball kavramlarına hakim olmak gerekir. Değişken tanımlarında söz konusu kavramlara kısaca değinilmiştir.
Her ne kadar değişkenlerde açıklansada beyzbolun nasıl oynandığı hakkında fikir edinmek gerekir.
    * CAtBat: Oyuncunun kariyeri boyunca sopa başına geçmesi.
    * CHits: Oyuncunun kariyeri boyunca toplam vuruş sayısı.
    * CHmRun: Oyuncunun kariyeri boyunca yaptığı toplam home run vuruş sayısı.
    * CRuns: Oyuncunun kariyeri boyunca yaptığı toplam sayı.
    * CRBI: Oyuncunun kariyeri boyunca vurucu görevindekiyen takıma kazandırdığı toplam puan.
    * CWalks: Oyuncunun kariyeri boyunca teknik faulden kazandığı toplam puan.
    * League: Oyuncunun ligi. A: Amerika Ligi; N: Ulusal Lig
    * Division: Oyuncunun bölgesi. E: Doğu, W: Batı
    * PutOuts: Oyuncunun alan öncesinde topu yakalama sayısı.
        Koşucu, kaleye gelmeden önce kale bekçisi topu yakalarsa putouts sayısı olur ve koşucu oyundan çıkar.
    * Assists: Oyuncusun yaptığı asist sayısı. Asist, kale bekçisine topu gönderen kişidir.
    * Errors: Oyuncunun havada tutamadığı top sayısı. Error, beyzbol topunu elden düşürmesine denir.
    * Salary: Oyuncunun dolar cinsinden maaşı.
    * NewLeague: Oyuncunun 1987 sezonu başındaki ligi.
"""

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import pickle
from helpers.data_prep import *
from helpers.eda import *
from helpers.helpers import *

pd.pandas.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 170)

def load_application_train():
    data = pd.read_csv(r"C:\Users\Suleakcay\PycharmProjects\pythonProject6\data\hitters.csv")
    return data

df = load_application_train()
df.head()


#Burada oyuncunun kariyeri boyunca aldığı maaşa(salary) etki eden faktörler genel itibariyle aşağıdaki durumlardan etkilenir
#Years:Oyuncunun yıl deneyimi
#CAtBat: Oyuncunun kariyeri boyunca sopa başına geçmesi.
#CHits: Oyuncunun kariyeri boyunca toplam vuruş sayısı.
#CRuns: Oyuncunun kariyeri boyunca yaptığı toplam sayı.
#CHmRun: Oyuncunun kariyeri boyunca yaptığı toplam home run vuruş sayısı.
#CRBI: Oyuncunun kariyeri boyunca vurucu görevindekiyen takıma kazandırdığı toplam puan.
#CWalks: Oyuncunun kariyeri boyunca teknik faulden kazandığı toplam puan.


grab_col_names(df)
"""
Observations: 322
Variables: 20
cat_cols: 3
num_cols: 17
cat_but_car: 0
num_but_cat: 0
Out[15]: 
(['League', 'Division', 'NewLeague'],
 [],
 ['AtBat',
  'Hits',
  'HmRun',
  'Runs',
  'RBI',
  'Walks',
  'Years',
  'CAtBat',
  'CHits',
  'CHmRun',
  'CRuns',
  'CRBI',
  'CWalks',
  'PutOuts',
  'Assists',
  'Errors',
  'Salary'],
 [])

"""
check_df(df) #veriyi inceledik
#shape :(322, 20)


#Salary değişkenindeki eksik gözlemleri median değeri ile doldurdum
df["Salary"]
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df.dropna(inplace=True)
df.isnull().sum()


df["RateCRun"] = df["CHmRun"] / df["CRuns"]
df["RateRun"] = df["HmRun"] / df["Runs"] #(homerun vuruş sayısı/toplam yaptığı sayı)
df["RateHit"] = df["Hits"] / df["AtBat"]
df["RateCHit"] = df["CHits"] / df["CAtBat"]


df["Average_CAtBatYear"] = df["CAtBat"] / df["Years"]
df["Average_CHitsYear"] = df["CHits"] / df["Years"]
df["Average_CRunsYear"] = df["CRuns"] / df["Years"]
df["Average_CHmRunYear"] = df["CHmRun"] / df["Years"]
df["Average_CRBIYear"] = df["CRBI"] / df["Years"]
df["Average_CWalksYear"] = df["CWalks"] / df["Years"]

df.loc[(df["Years"] <= 3), "Experience"] = "Elementary"
df.loc[(df["Years"] > 3) & (df["Years"] <= 8), "Experience"] = "Beginning"
df.loc[(df["Years"] > 8) & (df["Years"] <= 13), "Experience"] = "Normal"
df.loc[(df["Years"] > 13) & (df["Years"] <= 18), "Experience"] = "Experienced"
df.loc[(df["Years"] > 18), "Experience"] = "Vet"

df_new = df.copy()
df_new = df.drop(["AtBat", "Runs", "Division", "NewLeague", "HmRun", "Hits", "RBI", "League"], axis=1)

#Aykırı değerler
num_cols = [col for col in df_new.columns if len(df_new[col].unique()) > 18 and  df_new[col].dtypes != "O"]
df_new.shape #(322, 25)
for col in num_cols:
    replace_with_thresholds(df_new, col) #tepe değerden büyük değer varsa tepe değeri ile değiştirme işlemi gerçekleştirdim

#ONE-HOT ENCODING

def one_hot_encoder(dataframe, categorical_cols, drop_first=False):
    dataframe = pd.get_dummies(dataframe, columns=categorical_cols, drop_first=drop_first)
    return dataframe

ohe_cols = [col for col in df_new.columns if 10 >= len(df_new[col].unique()) > 2]

one_hot_encoder(df_new, ohe_cols).head()

one_hot_encoder(df_new, ohe_cols, drop_first=True).head()















