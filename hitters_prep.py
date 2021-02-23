"""
Değişkenleri anlamak için öncelikle baseball kavramlarına hakim olmak gerekir. Değişken tanımlarında söz konusu kavramlara kısaca değinilmiştir.
Her ne kadar değişkenlerde açıklansada beyzbolun nasıl oynandığı hakkında fikir edinmek gerekir.

    * AtBat: 1986 yılında oyuncunun vurucu (batter) olma sayısı.
        AtBat, topa vurmak üzere atıcının (pitcher) karşısına geçen oyuncudur.
    * Hits: 1986 yılında oyuncunun yaptığı başarılı faul olmadan vuruş sayısı.
        Vuruş sayısı, merkezde atıcının yaptığı atışa karşılık vurucunun sopa (bat) ile vurma durumu.
    * HmRun: 1986 yılında oyuncunun home run sayısı.
        Home run, beyzbolda en önemli sayıdır. Vurucunun topu saha dışarısına yollaması ile oluşan sayı turudur.
    * Runs: 1986 yılında oyuncunun yaptığı toplam sayı.
        Run (sayı), vurucu veya koşucunun (runner) oyundan çıkmadan tüm kaleleri dolaşıp sonuçta merkez kale levhasına dokunup sayı yapmasıdır.
    * RBI: 1986 yılında oyuncunun takıma kazandırdığı toplam sayı
    * Walks: 1986 yılında oyuncunun teknik faul sayesinde kazandığı toplam puan.
        Walks, atıcının 4 kez hatalı atması sonucu vurucunun bir sonraki kale (base) yürüyerek ulaşmasını sağlayan teknik fauldür.
    * Years: Oyuncunun yıl deneyimi.
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

pd.pandas.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 170)

def load_application_train():
    data = pd.read_csv(r"C:\Users\Suleakcay\PycharmProjects\pythonProject6\data\hitters.csv")
    return data

df = load_application_train()
df.head()

#Burada oyuncunun kariyeri boyunca aldığı maaşa etki eden faktörler genel itibariyle aşağıdaki durumlardan etkilenir
#Years:Oyuncunun yıl deneyimi
#CAtBat: Oyuncunun kariyeri boyunca sopa başına geçmesi.
#CHits: Oyuncunun kariyeri boyunca toplam vuruş sayısı.
#CRuns: Oyuncunun kariyeri boyunca yaptığı toplam sayı.
#CRBI: Oyuncunun kariyeri boyunca vurucu görevindekiyen takıma kazandırdığı toplam puan.
#CWalks: Oyuncunun kariyeri boyunca teknik faulden kazandığı toplam puan.

