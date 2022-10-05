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

path = (Path().home()/"Downloads"/"Topic_Extraction-main"
        /"Topic_Extraction-main"/"Data")   # you may need to change this path
file = os.listdir(path)

# create dataframe:
df = create_df(file)
print("DataFrame is created")

# preprocess the text:
df = preprocess(df)
print("Preprocessing is done")

# get most frequent words:
NUM = 30 # number of most frequent words
df = nlp(df, NUM) # most frequent words for every report
df_overall = nlp_overall(df, NUM) # most frequent words for all reports combined
# number of occurances a word has in the most frequent word list of the reports:
occurences = count_words(df, NUM)
print("first NLP analysis is done")

# get summaries:
# summary without the word "child", with max sentence legth of 50 and only the
# first 10 words of the most-frequent words list:
df = nlp2(df,1,50,10)
# summary with the word "child", with max sentence legth of 5000 and only the
# first 10 words of the most-frequent words list (not used in the project therefore commented):
#df2 = nlp2(df,0,5000,10)
print("sencond NLP analysis is done")

# saving dfs as excell files:
print("Saving DataFrames as excel files ...")

path = (Path().home()/"Downloads"/"Topic_Extraction-main"
        /"Topic_Extraction-main"/"results")  # you may need to cahnge this path
os.chdir(path)
df_overall.to_excel("df_overall.xlsx", encoding="utf-8-sig", index=False)
df.to_excel("df.xlsx", encoding="utf-8-sig", index=False)
occurences.to_excel("occurences.xlsx", encoding="utf-8-sig", index=False)
