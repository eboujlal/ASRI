import os
import pandas as pd
import string
import re
from cleaning import *
# Config
ORIGIN = "/home/iiraven/ASRI/raw_files/"
LM_ORIGIN = "/home/iiraven/ASRI/lm/"
DEV_SET = {'path':ORIGIN+"dev.tsv",'name':'dev'}
TEST_SET =  {'path':ORIGIN+"test.tsv",'name':'test'}
TRAIN_SET = {'path':ORIGIN+"train.tsv",'name':'train'}
OTHER_SET = {'path':ORIGIN+"other.tsv",'name':'other'}
INVALIDATED_SET = {'path':ORIGIN+"invalidated.tsv",'name':'invalidated'}
VALIDATED_SET = {'path':ORIGIN+"validated.tsv",'name':'validated'}
SETS = [DEV_SET,TEST_SET,TRAIN_SET,OTHER_SET,INVALIDATED_SET,VALIDATED_SET]

# Helpes
def load_files(path):
    df = pd.read_csv(path,delimiter="\t")
    return df

def create_text_file():
    with open(LM_ORIGIN+'lm_text.txt','w',encoding='utf-8') as f:
        pass
        
def save_text(text):
    with open(LM_ORIGIN+'lm_text.txt','a',encoding='utf-8') as f:
        f.write(text+" ")


# Generate text
create_text_file()
for path in SETS:
    print("** Start generating corpus from : "+path['name']+' dataset')
    df = load_files(path['path'])
    for index,row in df.iterrows():
        save_text(row.sentence+'\n')

print("Your copurs is ready in "+LM_ORIGIN+"lm_text.txt")