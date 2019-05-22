import os
import pandas as pd
from cleaning import *
# Dataset config
ORIGIN = "/home/iiraven/ASRI/"
DEV_SET = {'path':ORIGIN+"raw_files/dev.tsv",'name':'dev'}
TEST_SET =  {'path':ORIGIN+"raw_files/test.tsv",'name':'test'}
TRAIN_SET = {'path':ORIGIN+"raw_files/train.tsv",'name':'train'}
OTHER_SET = {'path':ORIGIN+"raw_files/other.tsv",'name':'other'}
INVALIDATED_SET = {'path':ORIGIN+"raw_files/invalidated.tsv",'name':'invalidated'}
VALIDATED_SET = {'path':ORIGIN+"raw_files/validated.tsv",'name':'validated'}
SETS = [DEV_SET,TEST_SET,TRAIN_SET,OTHER_SET,INVALIDATED_SET,VALIDATED_SET]

# Helpers
def load_files(path):
    return pd.read_csv(path,delimiter="\t")

for path in SETS:
    df = load_files(path.get('path'))
    data = []
    print("Preparing " + path['name']+' dataset')
    if len(df) == 0:
        continue
    for index,row in df.iterrows():
        
        data.append([
            ORIGIN+'dataset/wavs/'+row.path+".wav",
            os.stat(ORIGIN+'dataset/wavs/'+row.path+".wav").st_size,
            clean_text(row.sentence.lower())
            ])
    
        if index%1000 == 0:
            print(str(index)+" has been procceed")
            
    df_data = pd.DataFrame(data)
    df_data.columns = ['wav_filename','wav_filesize','transcript']
    df_data.to_csv(ORIGIN+'dataset/'+path.get('name')+'.csv',index=False)
    