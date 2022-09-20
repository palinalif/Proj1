import numpy as np
import pandas as pd
import seaborn as sb

df = pd.read_csv('smoke_detection_iot.csv')
# Remove missing values here, before we split it into X and y?
X = df.drop(["Unnamed: 0", "UTC", "CNT", "Fire Alarm"], axis=1)
y = df["Fire Alarm"]