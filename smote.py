import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as scp

df = pd.read_csv(r'c:\users\user\bank.csv', sep=';')
print(df.head())

print(df.describe())
print(df.info())
