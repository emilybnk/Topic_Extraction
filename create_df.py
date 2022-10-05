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

    # create empty dataframe with the coumns "year" and "text"
    array = np.empty([len(file), 2])
    array[:] = np.nan
    df_reports = pd.DataFrame(array)
    df_reports.columns = ["year", "text"]

    # fill columns with the data
    k = 0
    # iterate through the 40 reports/files
    for j in file:
        report = fitz.open(j)

        # get text of every page of the report and store it in page_str variable
        page_str = ""
        for page in report:
            page_str += page.get_text("text", sort=True)

        df_reports.iat[k,0] = j[-8:-4]  # year column
        df_reports.iat[k,1] = page_str  # text column

        k += 1
    return df_reports
