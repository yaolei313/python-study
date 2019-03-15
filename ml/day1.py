#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

dataset = pd.read_csv('/Users/yaolei/Work/100-Days-Of-ML-Code/datasets/Data.csv')

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values="NaN", strategy="mean")
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

ts1 = pd.Timestamp('20130102')
