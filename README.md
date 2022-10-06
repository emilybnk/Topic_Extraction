# Topic_Extraction

## Research questions
The goal of this project is to determine the topics Unicef deals with through the years and to compare these goals. This is done via topic extraction of the different annual reports of Unicef.
It was also investigated whether these topics match the topics on Unicef's website.

After that, a summary for every report is created in order to create context to the extracted words

## Data
The annual reports between 1982 and 2021 were used. They can be found here: https://www.unicef.org/unicef-annual-report
The filenames weren't all the same after the download, so I changed them manually into this format: UNICEF-annual-report-1982.
They can also be found in the data folder of this repository.

## Code
There are 5 code files.

"create_df.py": creates a dataframe with the year of the report in the first column and the text of the report in the second column

"preprocess.py": tokenizes, tags, lemmatizes the text and extract the nouns. Also, the stopwords were removed

"nlp.py": extracts the top 30 words per report and the top 30 words over all reports

"nlp2.py": creates an extractie summary for every report

"main.py": by running this code all tasks above are executed.

### Run the Code
In order to run the code, download the respository and unzip the foulder. In the main.py file change the directory if needed in order to process the data. Then execute all of the files mentioned above. Keep in mind to execute main.py last since this file loads functions from the other files.

## Results
In the results folder are the results of this project.

"df.xlsx": shows the top 30 words and summary per report

"df_overall.xlsx": shows the top 30 words over all reports

"occurences.xlsx": shows how often a word is part of the top 30 words of the reports. (40 reports --> max number occurences = 40)

## Requirements
The python version 3.9 was used.
The external packages that were used can be found in the "requirements.txt" file.
