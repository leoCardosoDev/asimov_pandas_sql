from pathlib import Path
import pandas as pd
import numpy as np

current_folder = Path(__file__).parent
df_obesity = pd.read_csv(current_folder / 'obesity_cleaned.csv')
print(df_obesity)

#to_frame ou []
print(type(df_obesity['Sex']))
print(type(df_obesity[['Sex']]))
print(type(df_obesity['Sex'].to_frame()))