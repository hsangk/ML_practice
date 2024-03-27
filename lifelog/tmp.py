import pandas as pd

def skip_col(df):
    df = df.iloc[:, 1:]
    return df

data_path = "./data/231023-DATA.xlsx"

DATA_USER = pd.read_excel(data_path, sheet_name='USER_ACCOUNT', skiprows=2)
DATA_USER = skip_col(DATA_USER)
date = DATA_USER['JOIN_TIME'].year
a = DATA_USER['JOIN_TIME'][0].date

for data in DATA_USER.iterrows():
    first_survey = str(data[2].year)[-2:] + str(data[2].month) + str(data[2].day)

print('done')