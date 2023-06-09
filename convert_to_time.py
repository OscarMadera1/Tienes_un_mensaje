from datetime import datetime
from read_csv import df
import pandas as pd



df['FechaNacimiento'] = pd.to_datetime(df['FechaNacimiento'],format="%Y/%m/%d")

df['year'] = df['FechaNacimiento'].dt.year
df['month'] = df['FechaNacimiento'].dt.month
df['day'] = df['FechaNacimiento'].dt.day

print(df['FechaNacimiento'].dt.day_name())