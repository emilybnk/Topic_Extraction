# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 13:25:00 2022

@author: emibu
"""

from pathlib import Path
import os
from create_df import create_df
from preprocess import preprocess
from nlp import nlp
from nlp import nlp_overall, count_words
from nlp2 import nlp2

path = (Path().home()/"Documents"/"Emily"/"Uni"/"Master"/"HHU"/"2. Semester"
        /"advanced NLP with Python"/"AP")
file = os.listdir(path)
df = create_df(file)
print("DataFrame is created")

df = preprocess(df)
print("Preprocessing is done")

NUM = 30
df = nlp(df, NUM)
df_overall = nlp_overall(df, NUM)
print("first NLP analysis is done")
words = count_words(df, NUM)

df = nlp2(df,1,50,10)
#df2 = nlp2(df,0,5000,10)
print("sencond NLP analysis is done")
print("Saving DataFrames as excel files ...")

path = (Path().home()/"Documents"/"Emily"/"Uni"/"Master"/"HHU"/"2. Semester"
        /"advanced NLP with Python")
os.chdir(path)
df_overall.to_excel("df_overall2.xlsx", encoding="utf-8-sig", index=False)
df.to_excel("df.xlsx", encoding="utf-8-sig", index=False)
