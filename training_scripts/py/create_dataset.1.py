import os
import pandas as pd
from cleaning import *
from sklearn.model_selection import train_test_split

# Dataset config
ORIGIN = "/home/iiraven/ASRI/"
DEV_SET = {'path':ORIGIN+"raw_files/dev.tsv",'name':'dev'}
TEST_SET =  {'path':ORIGIN+"raw_files/test.tsv",'name':'test'}
TRAIN_SET = {'path':ORIGIN+"raw_files/train.tsv",'name':'train'}
OTHER_SET = {'path':ORIGIN+"raw_files/other.tsv",'name':'other'}
INVALIDATED_SET = {'path':ORIGIN+"raw_files/invalidated.tsv",'name':'invalidated'}
VALIDATED_SET = {'path':ORIGIN+"raw_files/validated.tsv",'name':'validated'}
SETS = [DEV_SET,TEST_SET,TRAIN_SET,
        #OTHER_SET,INVALIDATED_SET,
        VALIDATED_SET]

# Helpers
def load_files(path):
    return pd.read_csv(path,delimiter="\t")

data = []
labels = []

for path in SETS:
    df = load_files(path.get('path'))
    print("Preparing " + path['name']+' dataset')
    if len(df) == 0:
        continue
    for index,row in df.iterrows():
        
        data.append([
            ORIGIN+'dataset/wavs/'+row.path+".wav",
            os.stat(ORIGIN+'dataset/wavs/'+row.path+".wav").st_size,
            clean_text(row.sentence.lower())
            ])
        labels.append(row.sentence.lower())
        if index%1000 == 0:
            print(str(index)+" has been procceed")
            

X_train, X_test, y_train, y_test = train_test_split(data, labels,test_size=0.1, random_state=1)

X_train, X_val, y_train, y_val  = train_test_split(X_train, y_train, test_size=0.13, random_state=1)

print("train " + str(len(X_train)) + "==>"+str(len(X_train) * 100 / len(data)))
print("dev " + str(len(X_val)) + "==>"+str(len(X_val) * 100 / len(data)))
print("test " + str(len(X_test)) + "==>"+str(len(X_test) * 100 / len(data)))
# Save training set
df_data = pd.DataFrame(X_train)
df_data.columns = ['wav_filename','wav_filesize','transcript']
df_data.to_csv(ORIGIN+'dataset/train.csv',index=False)

# Save dev set
df_data = pd.DataFrame(X_val)
df_data.columns = ['wav_filename','wav_filesize','transcript']
df_data.to_csv(ORIGIN+'dataset/dev.csv',index=False)

# Save test set
df_data = pd.DataFrame(X_test)
df_data.columns = ['wav_filename','wav_filesize','transcript']
df_data.to_csv(ORIGIN+'dataset/test.csv',index=False)