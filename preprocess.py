# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 09:32:07 2022

@author: emibu
"""

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def extract_nouns(text):
    """
    Parameters
    ----------
    text : TYPE: string
        string with the text of the report.

    Returns
    -------
    nouns_list : TYPE: list
        list of nouns.

    """
    token = nltk.word_tokenize(text)
    tag = nltk.pos_tag(token)
    noun_list = ["NN","NNS","NNPS","NNP"]
    nouns = [word for (word, pos) in tag if pos in noun_list]
    nouns_list = [noun.lower() for noun in nouns if len(noun)>2]
    return nouns_list

def lemmatize(nouns_list):
    """
    Parameters
    ----------
    nouns_list : TYPE: list
        list of nouns.

    Returns
    -------
    lemmatized : TYPE: list
        list of lemmatized nouns.

    """
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(w) for w in nouns_list]
    return lemmatized


def no_stopwords(lemmatized):
    """
    Parameters
    ----------
    text : TYPE: list
        list of lemmatized nouns.

    Returns
    -------
    no_stop : TYPE: list
        list of lemmatized nouns without the stopwords.

    """
    stop_words = stopwords.words("english")
    to_append = ["unicef","year","19",19,"report","annual","area","people","phc"
                 ,"cent","mr","co","’", "united","nations","nation","countries",
                 "tion","us","", "11_cc","inc","ar_2010_5","indd","new","every",
                 "ar_2010_5-11_cc.indd","inc.","reimagine","responding","years",
                 "unicefs","page"]
    stop_words += to_append
    no_stop = [word for word in lemmatized if not word.lower() in stop_words]
    return no_stop


def preprocess(df_preprocess):
    """
    Parameters
    ----------
    df_preprocess : TYPE: DataFrame
        takes the dataframe that was created in create_df.py.

    Returns
    -------
    df_preprocess : TYPE: DataFrame
        returns the preprocessed dataframe.

    """
    df_preprocess["list_nouns"] = df_preprocess["text"].apply(extract_nouns)
    df_preprocess["lemmatized"] = df_preprocess["list_nouns"].apply(lemmatize)
    df_preprocess["list_w/o_stop"] = df_preprocess["lemmatized"].apply(no_stopwords)

    df_preprocess = df_preprocess.astype({"year":"int"})
    return df_preprocess
