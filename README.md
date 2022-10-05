# Topic_Extraction

## Research questions
The goal of this project is to determine the topics Unicef deals with through the years and to compare these goals. This is done via topic extraction of the different annual reports of Unicef.
It was also investigated whether these topics match the topics on Unicef's website.

After that, a summary for every report is created in order to create context to the extracted words

## Data
The annual reports between 1982 and 2021 were used. They can be found here: https://www.unicef.org/unicef-annual-report
The filenames weren't the same after the download, so I changed them manually into this format: UNICEF-annual-report-1982

## Code
There are 5 code files.
"create_df.py": creates a dataframe with the year of the report in the first column and the text of the report in the second column

"preprocess.py": tokenizes, tags, lemmatizes the text and extract the nouns. Also, the stopwords were removed

"nlp.py": extracts the top 30 words per report and the top 30 words over all reports

"nlp2.py": creates an extractie summary for every report

"main.py": by running this code all tasks above are executed (before, all the other files have to be executed so that main.py is able to load their functions)

## Requirements
The requirements can be found in the "requirements.txt" file
