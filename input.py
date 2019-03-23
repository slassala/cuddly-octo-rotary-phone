# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 13:19:36 2019

@author: maria.lassala
"""

import pandas as pd
import os

CSV_PATH = os.path.join('..','collection-master', 'artwork_data.csv')
CSV_PATH


COLS_TO_USE=['id','all_artists','title','medium','acquisitionYear','height','width','units']

COLS_TO_USE_csv=['id','artist','title','medium','acquisitionYear','height','width','units']

my_csv7=pd.read_csv('C:/Users/maria.lassala/Desktop/MISDOCs/python/pandas/collection-master/collection-master/artwork_data.csv', nrows=7,
                   index_col='id', usecols=COLS_TO_USE_csv)

my_csv=pd.read_csv('C:/Users/maria.lassala/Desktop/MISDOCs/python/pandas/collection-master/collection-master/artwork_data.csv',
                   index_col='id', usecols=COLS_TO_USE_csv)

df.to_pickle('C:/Users/maria.lassala/Desktop/MISDOCs/python/pandas/collection-master/collection-master/data_frame.pickle')

records=[("Expresso", "5$"),("Flat White", "$20")]
pd.DataFrame.from_records(records)
df_coffee = pd.DataFrame.from_records(records,columns=["Coffee","Price"])

def get_record_from_file(file_path, keys_to_use):
    import json
    
    with open(file_path) as artwork_file:
        content = json.load(artwork_file)
        
    record=[]
    for field in keys_to_use:
        record.append(content[field])
    return tuple(record)

sample_record=get_record_from_file('C:/Users/maria.lassala/Desktop/MISDOCs/python/pandas/collection-master/collection-master/artworks/a/000/a00001-1035.json',COLS_TO_USE)

json_root=os.path.join('C:/Users/maria.lassala/Desktop/MISDOCs/python/pandas/collection-master/','collection-master/', 'artworks')
json_root

artworks=[]

def reads_artworks_from_json(keys_to_use):
    for root,_,files in os.walk(json_root):
        for f in files:
            if f.endswith ('json'):
                record=get_record_from_file(os.path.join(root,f), keys_to_use)
                artworks.append(record)
        break
    df=pd.DataFrame.from_records(artworks,columns=keys_to_use,index="id")
    return df

    
df_2=reads_artworks_from_json(COLS_TO_USE)

   
        
artworks
minuto 5.45 tate collection metadata