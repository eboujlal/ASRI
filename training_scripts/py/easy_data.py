import os
import pandas as pd
from cleaning import *
from sklearn.model_selection import train_test_split
# Dataset config
ORIGIN = "/home/iiraven/ASRI/"
DEV_SET = {'path':ORIGIN+"raw_files/dev.tsv",'name':'dev'}

# Helpers
def load_files(path):
    return pd.read_csv(path,delimiter="\t",nrows=2000)

df = load_files(DEV_SET.get('path'))
data = []
print("Preparing dataset")
labels = []
for index,row in df.iterrows():
    text = clean_text(row.sentence.lower())
    data.append([
        ORIGIN+'dataset/wavs/'+row.path+".wav",
        os.stat(ORIGIN+'dataset/wavs/'+row.path+".wav").st_size,
        text
        ])
    labels.append(text)
    if index%1000 == 0:
        print(str(index)+" has been procceed")

X_train, X_test, y_train, y_test = train_test_split(data, labels,test_size=0.2, random_state=1)

X_train, X_val, y_train, y_val  = train_test_split(X_train, y_train, test_size=0.2, random_state=1)

datasets = ['DEV','TRAIN','TEST']

# Save training set
df_data = pd.DataFrame(X_train)
df_data.columns = ['wav_filename','wav_filesize','transcript']
df_data.to_csv(ORIGIN+'dataset_easy/train.csv',index=False)

# Save dev set
df_data = pd.DataFrame(X_val)
df_data.columns = ['wav_filename','wav_filesize','transcript']
df_data.to_csv(ORIGIN+'dataset_easy/dev.csv',index=False)

# Save test set
df_data = pd.DataFrame(X_test)
df_data.columns = ['wav_filename','wav_filesize','transcript']
df_data.to_csv(ORIGIN+'dataset_easy/test.csv',index=False)