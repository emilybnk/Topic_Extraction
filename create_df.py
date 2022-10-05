# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 07:45:02 2022

@author: emibu
"""
from pathlib import Path
import os
import pandas as pd
import numpy as np
import fitz


def create_df(file):
    """
    Parameters
    ----------
    file : list
        list of pdf-file names.

    Returns
    -------
    df_reports : DataFrame
        dataframe with the columns "year" and "text" and a row for each report.

    """
    path = (Path().home()/"Documents"/"Emily"/"Uni"/"Master"/"HHU"
            /"2. Semester"/"advanced NLP with Python"/"AP")
    os.chdir(path)

    array = np.empty([len(file), 2])
    array[:] = np.nan
    df_reports = pd.DataFrame(array)
    df_reports.columns = ["year", "text"]

    k = 0
    for j in file:
        report = fitz.open(j)

        page_str = ""
        for page in report:
            page_str += page.get_text("text", sort=True)

        df_reports.iat[k,0] = j[-8:-4]
        df_reports.iat[k,1] = page_str

        k += 1
    return df_reports
