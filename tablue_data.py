# -*- coding: utf-8 -*-
"""Tablue_data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S0XPz2wLvG5tqFkxO3Ds6e091l1Gfbr_
"""

!pip install requests -q

import numpy as np
import pandas as pd
import requests

Url = "https://cea.nic.in/api/electricEnergySales.php"

response = requests.get(Url)

if response.status_code == 200:
  data = response.json()
  df = pd.DataFrame(data)
  print("Data is ready...")
else:
  print(f"Failed to fetch the data. Status code: {response.status_code}")

# Top five records in the dataframe
df.head()

df.info()

# Null values
df.isnull().sum()

df.groupby('State').size().reset_index()

df['State'] = df['State'].replace({'[\.\$]':''}, regex=True)

df.groupby('State').size().reset_index()

df['State'] = df['State'].str.strip()

df.groupby('State').size().reset_index()

df['State'] = df['State'].replace('Madhay Pradesh', 'Madhya Pradesh')

df.groupby('State').size().reset_index()

df['State'] = df['State'].replace('Orissa', 'Odisha')

df.groupby('State').size().reset_index()

df.head()

df.to_csv('energy_sales.csv', index_label=False)