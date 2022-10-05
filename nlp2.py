# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:26:24 2022

@author: emibu
"""

from nltk import tokenize
from nlp import top_words
import numpy as np


def get_sent(text,words,length):
    """
    Parameters
    ----------
    text : str
        string with the text of the report.
    words : TYPE: list
        list of most frequent words of one report.
    length : TYPE: int
        max number of words of sentence.

    Returns
    -------
    final_list : TYPE: list
        list of sentences which have the words in it (summary).

    """
    # https://stackoverflow.com/questions/67679280/how-to-extract-sentences-of-text-that-contain-keywords-in-list
    sent = tokenize.sent_tokenize(text)
    sentences = [sentence for sentence in sent if any(w.lower() in sentence.lower() for w in words)]

    new_list = [s.replace("\n", "") for s in sentences]
    new_list = [s.replace(",", "") for s in new_list]
    final_list = [x for x in new_list if len(x.split())<length]
    return final_list


def nlp2(df, stop, length, num):
    """
    Parameters
    ----------
    df : TYPE: DataFrame
        takes dataframe that is generated in nlp.
    stop : TYPE: int
        whether the word "child" should be excluded (stop=1) or not.
    length : TYPE: int
        max number of words of sentence.
    num : TYPE: int
        number of words of the most-frequent-word list that should be included.

    Returns
    -------
    df : TYPE: DataFrame
        returns a dataframe with the "summary" column, a colun with the length
        of the summary, the proportion the summary has in respect to the original
        document, the mean length of the summary and the standard deviation.

    """
    array = np.empty([len(df), 1])
    df["summary"] = array
    loc = df.columns.get_loc("summary")

    # get top words of each report
    for i in range(len(df)):
        words =[top_words(df["list_w/o_stop"][i],"words",k) for k in range(num)]

        if stop == 1:
            stop_words = ["child"]
            words = [w for w in words if not w.lower() in stop_words]
            df.iat[i,loc] = get_sent(df["text"][i],words,length)
        else:
            df.iat[i,loc] = get_sent(df["text"][i],words,length)

    df["length 2"] = df["summary"].apply(lambda x: len(" ".join(x).split()))
    df["percentage"] = df["length 2"]/df["length"] *100
    print("mean summary length:", df["percentage"].mean(), "%")
    print("std:", df["percentage"].std(), "%")

    return df
