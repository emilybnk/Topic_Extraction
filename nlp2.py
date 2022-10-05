# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:26:24 2022

@author: emibu
"""

from nltk import tokenize
import numpy as np
from nlp import top_words


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

    sent = tokenize.sent_tokenize(text) # tokenize text into sentences
    # get sentences of text that contain keywords:
    # the following line of code is from:
    # https://stackoverflow.com/questions/67679280/how-to-extract-sentences-of-text-that-contain-keywords-in-list
    sentences = [sentence for sentence in sent if any(w.lower() in sentence.lower() for w in words)]

    # remove pragraphs and commas in order to get a better reading flow
    new_list = [s.replace("\n", "") for s in sentences]
    new_list = [s.replace(",", "") for s in new_list]
    # remove sentences that have more than "length" words in it
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
    # creae empty df column and its loaction in the df
    array = np.empty([len(df), 1])
    df["summary"] = array
    loc = df.columns.get_loc("summary")

    # get top words of each report
    for i in range(len(df)):
        words =[top_words(df["list_w/o_stop"][i],"words",k) for k in range(num)]

        # remoce stopword "child" wanted
        if stop == 1:
            stop_words = ["child"]
            words = [w for w in words if not w.lower() in stop_words]
            # get sentence of the words that are in the "words" list
            df.iat[i,loc] = get_sent(df["text"][i],words,length)
        else:
            df.iat[i,loc] = get_sent(df["text"][i],words,length)

    # length of summary:
    df["length 2"] = df["summary"].apply(lambda x: len(" ".join(x).split()))
    # get the proportion the summary has in respect to the original text:
    df["percentage"] = df["length 2"]/df["length"] *100
    # get mean summary length
    print("mean summary length:", df["percentage"].mean(), "%")
    # get standard deviation of mean summary length
    print("std:", df["percentage"].std(), "%")

    return df
