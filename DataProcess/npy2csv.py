# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
import os.path

import  numpy as np
import pandas as pd


DF_NAMES=["path_dir"]

def make_dataframe(nbr_rows=None, df_names=DF_NAMES):
    """
    Create empty frames metadata pandas dataframe given number of rows
    and standard column names defined below

    :param [None, int] nbr_rows: The number of rows in the dataframe
    :param list df_names: Dataframe column names
    :return dataframe frames_meta: Empty dataframe with given
        indices and column names
    """

    if nbr_rows is not None:
        # Create empty dataframe
        frames_meta = pd.DataFrame(
            index=range(nbr_rows),
            columns=df_names,
        )
    else:
        frames_meta = pd.DataFrame(columns=df_names)
    return frames_meta


a=np.load("resultsData/record.npy", allow_pickle=True)
record=a.tolist()
print(record)

frames_meta=make_dataframe(nbr_rows=len(record))

for i in range(len(record)):
    meta_row=dict.fromkeys(DF_NAMES)
    meta_row["path_dir"]=record[i]
    frames_meta.loc[i]=meta_row

frames_meta_filename=os.path.join("../", "testdata/frame_meta.csv")

frames_meta.to_csv(frames_meta_filename,sep=",")

