# -*- coding: utf-8 -*-
"""tensorflow_datasets .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KyEeqNL-BtS7X4NV2rvOuWOAtsoWNwGL

# Dummy data available in `tensorflow_datasets` module
"""

# import tensorflow_datasets
import tensorflow_datasets as tfds
import pandas as pd

# Get list of datasets
tfds.list_builders()

# Pick any dataset from the list & find dataset info.
ds = tfds.builder('titanic')
ds.info
# Inside DatasetInfo object find homepage or url tag to download csv data manually.

# Find data.csv donwload link in that webpage. And read csv using pandas dataFrame
df = pd.read_csv('https://www.openml.org/data/get_csv/16826755/phpMYEkMl')
df
# OpenML(https://www.openml.org/) is a good open source resource of csv data.

df = tfds.builder('diabetic_retinopathy_detection')
df.info

df = tfds.builder('trec')
df.info