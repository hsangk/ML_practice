import pandas as pd
import numpy as np
from labeling import label_dict

def skip_col(df):
    df = df.iloc[:, 1:]
    return df

def encode_weekly_survey(df: pd.DataFrame, col_name: str):
    encoded_result = []
    orig_data = df[col_name].values
    if col_name == 'QUESTION_RESULT_2':
        for data in orig_data:
            if data == 2:
                encoded = 4
            elif data == 4:
                encoded = 2
            else:
                encoded = data
            encoded_result.append(encoded)

    elif col_name == 'QUESTION_RESULT_6':
        for data in orig_data:
            if data == 1: encoded = 6
            elif data == 2: encoded = 5
            elif data == 3: encoded = 4
            elif data == 4: encoded = 3
            elif data == 5: encoded = 2
            else: encoded = 1
            encoded_result.append(encoded)
    return encoded_result

def encode_daily_survey(df: pd.DataFrame, col_name: str):
    encoded_result = []
    orig_data = df[col_name].values
    for data in orig_data:
        if data == 1: encoded = 2
        elif data == 2: encoded = 1
        encoded_result.append(encoded)
    return encoded_result

def discrete_survey(df: pd.DataFrame, col_name: str):
    encoded_result = []
    orig_data = df[col_name].values
    for data in orig_data:
        if data == 1: encoded = 2
        elif data == 2: encoded = 1
        encoded_result.append(encoded)
    return encoded_result

def preprocess(data_path, label_path):
    DATA_USER = pd.read_excel(data_path, sheet_name='USER_ACCOUNT', skiprows=2)
    DATA_WEEKLY = pd.read_excel(data_path, sheet_name='WEELKLY SURVEY', skiprows=2)
    DATA_DAILY = pd.read_excel(data_path, sheet_name='DAILY SURVEY', skiprows=2)
    DATA_CALLS = pd.read_excel(data_path, sheet_name='CALLS', skiprows=2)
    DATA_DECIBEL = pd.read_excel(data_path, sheet_name='DECIBEL', skiprows=2)
    DATA_LUX = pd.read_excel(data_path, sheet_name='LUX', skiprows=2)
    DATA_MESSAGE = pd.read_excel(data_path, sheet_name='MESSAGE', skiprows=2)
    DATA_PICTURE = pd.read_excel(data_path, sheet_name='PICTURE', skiprows=2)
    DATA_SLEEP = pd.read_excel(data_path, sheet_name='SLEEP', skiprows=2)
    DATA_STEP = pd.read_excel(data_path, sheet_name='STEP', skiprows=2)
    DATA_APP = pd.read_excel(data_path, sheet_name='APPS', skiprows=2)

    DATA_USER = skip_col(DATA_USER)
    DATA_WEEKLY = skip_col(DATA_WEEKLY)
    DATA_DAILY = skip_col(DATA_DAILY)
    DATA_CALLS = skip_col(DATA_CALLS)
    DATA_DECIBEL = skip_col(DATA_DECIBEL)
    DATA_LUX = skip_col(DATA_LUX)
    DATA_MESSAGE = skip_col(DATA_MESSAGE)
    DATA_PICTURE = skip_col(DATA_PICTURE)
    DATA_SLEEP = skip_col(DATA_SLEEP)
    DATA_STEP = skip_col(DATA_STEP)
    DATA_APP = skip_col(DATA_APP)

    DATA_USER.drop(
        columns=['USER_NAME', 'LAST_ACCESS_TIME', 'FIRST_SURVEY_FLAG', 'SECOND_SURVEY_FLAG', 'THIRD_SURVEY_FLAG'],
        inplace=True)
    id_list = []
    first_survey_list = []
    second_survey_list = []
    third_survey_list = []
    for data in DATA_USER.iterrows():
        id_list.append(data[1][0])
        first_survey_list.append(data[1][1].strftime("%Y%m%d"))
        second_survey_list.append(data[1][2].strftime("%Y%m%d"))
        third_survey_list.append(data[1][3].strftime("%Y%m%d"))
    # 여기 ID 리스트 생성
    DATA_USER['first_survey'] = first_survey_list
    DATA_USER['second_survey'] = second_survey_list
    DATA_USER['third_survey'] = third_survey_list
    DATA_USER.drop(DATA_USER.columns[1:4], axis=1, inplace=True)
    week_dict = {id_list[i]: (first_survey_list[i], second_survey_list[i], third_survey_list[i]) for i in range(len(id_list))}


    # 2번 문항만 : 2-1, 2-2, 2-3, 2-4 (이산형)
    # DATA_WEEKLY['QUESTION_RESULT_2'] = encode_weekly_survey(DATA_WEEKLY, 'QUESTION_RESULT_2')
    DATA_WEEKLY['QUESTION_RESULT_6'] = encode_weekly_survey(DATA_WEEKLY, 'QUESTION_RESULT_6')
    DATA_WEEKLY.drop(labels='QUESTION_RESULT_1_2', axis=1, inplace=True)
    DATA_WEEKLY.drop(labels='QUESTION_RESULT_1_2_1', axis=1, inplace=True)
    DATA_WEEKLY.drop(labels='QUESTION_RESULT_3_1', axis=1, inplace=True)
    DATA_WEEKLY['QUESTION_RESULT_2'] = DATA_WEEKLY['QUESTION_RESULT_2'].astype(str)
    DATA_WEEKLY = pd.get_dummies(DATA_WEEKLY, columns=['QUESTION_RESULT_2'], prefix='QUESTION_RESULT_2')

    tmp_data = []
    for _, row in DATA_WEEKLY.iterrows():
        row[1] = week_dict[row[0]][row[1]-1]
        tmp_data.append({'USER_ID': row[0], 'date': row[1]})
    tmp_df = pd.DataFrame(tmp_data)
    DATA_WEEKLY.drop(labels='USER_ID', axis=1, inplace=True)
    DATA_WEEKLY.drop(labels='SURVEY_SEQUENCE', axis=1, inplace=True)
    DATA_WEEKLY = pd.concat([tmp_df,DATA_WEEKLY], axis=1)


    DATA_DAILY['TODAY_QUESTION_RESULT_3'] = encode_daily_survey(DATA_DAILY, 'TODAY_QUESTION_RESULT_3')
    DATA_DAILY['TODAY_QUESTION_RESULT_4'] = encode_daily_survey(DATA_DAILY, 'TODAY_QUESTION_RESULT_4')
    DATA_DAILY['TODAY_QUESTION_RESULT_5'] = encode_daily_survey(DATA_DAILY, 'TODAY_QUESTION_RESULT_5')
    DATA_DAILY['TODAY_QUESTION_RESULT_6'] = encode_daily_survey(DATA_DAILY, 'TODAY_QUESTION_RESULT_6')
    DATA_DAILY['TODAY_QUESTION_RESULT_7'] = encode_daily_survey(DATA_DAILY, 'TODAY_QUESTION_RESULT_7')
    DATA_DAILY['TODAY_QUESTION_RESULT_8'] = encode_daily_survey(DATA_DAILY, 'TODAY_QUESTION_RESULT_8')
    DATA_DAILY.drop(labels='STATE_SCORE', axis=1, inplace=True)
    # DATA_DAILY['daily_score'] = DATA_DAILY.iloc[:, 2:].sum(axis=1)
    # DATA_DAILY = DATA_DAILY.drop(DATA_DAILY.columns[2:-1], axis=1)
    DATA_DAILY.rename(columns={'STATE_DATE': 'date'}, inplace=True)
    DATA_DAILY['date'] = DATA_DAILY['date'].apply(str)

    DATA_CALLS['CALL_DATE'] = DATA_CALLS['CALL_DATE'].apply(lambda x: str(x)[:8])
    DATA_CALLS = DATA_CALLS.groupby(['USER_ID', 'CALL_DATE'])['CALL_DURATION'].agg(['sum'])
    DATA_CALLS.reset_index(drop=False, inplace=True)
    DATA_CALLS.rename(columns={'sum': 'call_duration', 'CALL_DATE': 'date'}, inplace=True)

    DATA_DECIBEL['DB_TIME'] = DATA_DECIBEL['DB_TIME'].apply(lambda x: str(x)[:8])
    DATA_DECIBEL = DATA_DECIBEL.groupby(['USER_ID', 'DB_TIME'])['DB_VALUE'].agg(['mean', 'max', 'min'])
    DATA_DECIBEL.reset_index(drop=False, inplace=True)
    DATA_DECIBEL.rename(columns={'mean': 'db_value_mean', 'max': 'db_value_max', 'min': 'db_value_min', 'DB_TIME': 'date'}, inplace=True)

    DATA_LUX['LUX_TIME'] = DATA_LUX['LUX_TIME'].apply(lambda x: str(x)[:8])
    DATA_LUX = DATA_LUX.groupby(['USER_ID', 'LUX_TIME'])['LUX_VALUE'].agg(['mean', 'max', 'min'])
    DATA_LUX.reset_index(drop=False, inplace=True)
    DATA_LUX.rename(columns={'mean': 'lux_value_mean', 'max': 'lux_value_max', 'min': 'lux_value_min','LUX_TIME':'date'}, inplace=True)

    DATA_MESSAGE['MESSAGE_DATE'] = DATA_MESSAGE['MESSAGE_DATE'].apply(lambda x: str(x)[:8])
    DATA_MESSAGE = DATA_MESSAGE.groupby(['USER_ID', 'MESSAGE_DATE'])['MESSAGE_NUMBER'].agg(['count'])
    DATA_MESSAGE.reset_index(drop=False, inplace=True)
    DATA_MESSAGE.rename(columns={'count': 'msg_num', 'MESSAGE_DATE': 'date'}, inplace=True)

    DATA_PICTURE['PICTURE_DATE'] = DATA_PICTURE['PICTURE_DATE'].apply(lambda x: str(x)[:8])
    DATA_PICTURE = DATA_PICTURE.groupby(['USER_ID', 'PICTURE_DATE'])['PICTURE_TITLE'].agg(['count'])
    DATA_PICTURE.reset_index(drop=False, inplace=True)
    DATA_PICTURE.rename(columns={'count': 'pic_num', 'PICTURE_DATE': 'date'}, inplace=True)

    DATA_SLEEP['START_TIME'] = DATA_SLEEP['START_TIME'].apply(lambda x: str(x)[:8])
    DATA_SLEEP['SLEEP_TIME'] = DATA_SLEEP['SLEEP_TIME'].apply(lambda x: x//60)
    DATA_SLEEP = DATA_SLEEP.groupby(['USER_ID', 'START_TIME'])['SLEEP_TIME'].agg(['sum'])
    DATA_SLEEP.reset_index(drop=False, inplace=True)
    DATA_SLEEP.rename(columns={'sum': 'sleep_duration', 'START_TIME': 'date'}, inplace=True)

    DATA_STEP['STEP_DATE'] = DATA_STEP['STEP_DATE'].apply(lambda x: str(x)[:8])
    DATA_STEP = DATA_STEP.groupby(['USER_ID', 'STEP_DATE'])['STEP_COUNT'].agg(['sum'])
    DATA_STEP.reset_index(drop=False, inplace=True)
    DATA_STEP.rename(columns={'sum': 'step_count', 'STEP_DATE': 'date'}, inplace=True)

    DATA_APP['COLLECT_DATE'] = DATA_APP['COLLECT_DATE'].apply(lambda x:str(x)[:8])
    DATA_APP = DATA_APP.groupby(['USER_ID', 'COLLECT_DATE']).sum()
    DATA_APP.reset_index(drop=False, inplace=True)
    DATA_APP.rename(columns={'ACC_COUNT': 'app_acc', 'AUDIO_COUNT': 'app_audio', 'GAME_COUNT': 'app_game', 'IMAGE_COUNT': 'app_img', 'MAPS_COUNT': 'app_maps', 'NEWS_COUNT': 'app_news', 'VIDEO_COUNT': 'app_video', 'COLLECT_DATE': 'date'}, inplace=True)
    DATA_APP.drop(['SOCIAL_COUNT'], axis=1, inplace=True)

    DATA = pd.merge(DATA_CALLS, DATA_DECIBEL, how='outer', on=['USER_ID', 'date'])
    DATA = pd.merge(DATA, DATA_LUX, how='outer', on=['USER_ID', 'date'])
    DATA = pd.merge(DATA, DATA_MESSAGE, how='outer', on=['USER_ID', 'date'])
    DATA = pd.merge(DATA, DATA_PICTURE, how='outer', on=['USER_ID', 'date'])
    DATA = pd.merge(DATA, DATA_SLEEP, how='outer', on=['USER_ID', 'date'])
    DATA = pd.merge(DATA, DATA_STEP, how='outer', on=['USER_ID', 'date'])
    DATA = pd.merge(DATA, DATA_DAILY, how='outer', on=['USER_ID', 'date'])
    DATA = pd.merge(DATA, DATA_WEEKLY, how='outer', on=['USER_ID', 'date'])
    # result = pd.merge(result, DATA_APP, how='outer', on=['USER_ID', 'date'])


    label = label_dict(label_path)
    label_list = []

    for _, data in DATA.iterrows():
        if str(data[0]) not in label.keys():
            label_list.append(0)
        else:
            label_list.append(label[str(data[0])])

    DATA['label'] = label_list


    tmp2_data = []
    for _, row in DATA.iterrows():
        if pd.isna(row[-2]) and row[1] in week_dict:
            if int(row[1]) >= int(week_dict[row[0]][0]) and int(row[1]) < int(week_dict[row[0]][1]):
                tmpf = tmp_df[(tmp_df['USER_ID'] == row[0]) & (tmp_df['date'] == week_dict[row[0]][0])]
                tmp2_data.append(tmpf['weekly_score'])
            elif int(row[1]) >= int(week_dict[row[0]][1]) and int(row[1]) < int(week_dict[row[0]][2]):
                tmpf = tmp_df[(tmp_df['USER_ID'] == row[0]) & (tmp_df['date'] == week_dict[row[0]][1])]
                tmp2_data.append(tmpf['weekly_score'])
            elif int(row[1]) >= int(week_dict[row[0]][2]) and int(row[1]) < (int(row[1])+100):
                tmpf = tmp_df[(tmp_df['USER_ID'] == row[0]) & (tmp_df['date'] == week_dict[row[0]][2])]
                tmp2_data.append(tmpf['weekly_score'])
            else:
                tmp2_data.append(np.nan)
        else:
            tmp2_data.append(row[-2])

    DATA['weekly_score'] = tmp2_data


    return DATA

if __name__ == '__main__':
    data_path = "./data/231023-DATA.xlsx"
    label_path = "./data/231024-label.xlsx"
    DATA = preprocess(data_path, label_path)
    DATA.to_csv("./data/result.csv", mode='w')