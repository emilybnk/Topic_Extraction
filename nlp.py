# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 10:12:24 2022

@author: emibu
"""

import pandas as pd
import numpy as np


def top_words(nouns,i,k):
    """
    Parameters
    ----------
    nouns : TYPE: list
        list of lemmatized nouns without stopwords.
    i : TYPE: string
        whether you want the word itself of its quantity.
    k : TYPE: string
        the kth most frequent word/quantity.

    Returns
    -------
    TYPE: string
        word or quantity.

    """
    words = pd.value_counts(np.array(nouns)) # count how often a noun appears in the list "noun"
    words = words.reset_index(level=0)  # because the words have been the index of the df
    words = words.rename(columns={"index":"words",0:"quantity"}) # rename column names
    return words[i][k]


def top_words_overall(nouns, i, k, num):
    """
    Parameters
    ----------
    nouns : TYPE: list
        list of lemmatized nouns without stopwords.
    i : TYPE: string
        whether you want the word itself of its quantity.
    k : TYPE: string
        the kth most frequent word/quantity.
    num : TYPE: int
        number of words that should be returned.

    Returns
    -------
    TYPE: string
        word or quantity.

    """
    # combine all nouns (i.e., of every year) into one list:
    list_all_nouns = sum([nouns[j] for j in range(40)],[])
    # count how often a noun appears in the list "list_all_nouns":
    words = pd.value_counts(np.array(list_all_nouns))[0:num]
    # because the words have been the index of the df:
    words = words.reset_index(level=0)
    # rename column names:
    words = words.rename(columns={"index":"words",0:"quantity"})
    return words[i][k]


def nlp(df, num):
    """
    Parameters
    ----------
    df : TYPE: DataFrame
        takes dataframe that is generated in preprocess.py.
    num : TYPE: int
        number of words that should be returned.

    Returns
    -------
    df : TYPE: DataFrame
        dataframe with the most frequent words for each report report.

    """
    # get 30 most frequent words and the quantity for every year:
    for k in range(num):
        df["top word" + str(k+1)] = df["list_w/o_stop"].apply(lambda x: top_words(x,"words",k))
        df["quantity" + str(k+1)] = df["list_w/o_stop"].apply(lambda x: top_words(x,"quantity",k))
    df["length"] = df["text"].apply(lambda x: len(x.split()))
    return df


def count_words(df, num):
    """
    Parameters
    ----------
    df : TYPE: DataFrame
        takes dataframe that is returned in the nlp funciton.
    num : TYPE: int
        number of words that should be returned.

    Returns
    -------
    words : TYPE: Series
        list of words with their number of occurenes in the "most-frequent-words"-
        columns of the reports (between 1 and 40 occurences since there are 40 reports.

    """
    # store all the nouns that are under the 30-most-frequent-nouns of each report in one list:
    words = []
    for i in range(num):
        for k in range(40): # 40 reports
            words.append(df["top word"+str(i+1)][k])
    # count how often a noun appears in the list "list_all_nouns":
    words = pd.value_counts(np.array(words))
    words = pd.DataFrame(words) # convert to df
    words = words.reset_index(level=0)  # because the words have been the index of the df
    words = words.rename(columns={"index":"words",0:"occurences"}) # rename column names
    return words


def nlp_overall(df, num):
    """
    Parameters
    ----------
    df : TYPE: DataFrame
        takes dataframe that is generated in preprocess.py.
    num : TYPE: int
        number of words that should be returned.

    Returns
    -------
    df_overall : TYPE: DataFrame
        dataframe with the most frequent words over all reports.

    """
    # create empty df
    array = np.empty([4,2*num+1])
    array[:] = np.nan
    df_overall = pd.DataFrame(array)
    df_overall.iat[0,0] = "All"

    # get the 30 most frequent words and the quantity overall by using the above function
    for k in range(num):
        df_overall.iat[0, 2*k+1] = top_words_overall(df["list_w/o_stop"], "words", k, num)
        df_overall.iat[0, 2*k+2] = top_words_overall(df["list_w/o_stop"], "quantity", k, num)

    liste = ["word", "quantity"]
    df_overall.columns = ["year"] + num*liste # change column names
    return df_overall
