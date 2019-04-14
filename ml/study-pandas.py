#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

# pd.Series一维数据，带有标签的同构类型数组
# 第一列是数据的索引，被称为index
s1 = pd.Series([1, 3, 5, np.nan, 7, 9])
print("series s1:\n{}".format(s1))
print("s1.value {}\ns1.index {}".format(s1.values, s1.index))
print("series s1:\n{}".format(s1.dropna()))
print("series s1 fillna:\n{}".format(s1.fillna(100)))

s2 = pd.Series([1, 3, 5, 7], index=['A', 'B', 'C', 'G'])
print("series s2:\n%s" % s2)

dates = pd.date_range('20180313', periods=6)
print("dates:\n{}".format(dates), end='\n===============\n\n')

print("{}\n{}".format(np.arange(12), np.arange(12).reshape(3, 4)))

# DataFrame二维数据，带index及columns
# 不同column可以是不同的数据类型
df1 = pd.DataFrame(np.arange(16).reshape(4, 4))
print("df1:\n{}".format(df1))

df2 = pd.DataFrame(np.arange(16).reshape(4, 4), index=["a", "b", "c", "d"], columns=["column1", "column2", "column3", "column4"])
print("df2:\n{}".format(df2))

# pd.Categorical有效地编码了包含大量重复文本的数据
# dict的key会变成column
df3 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('19870313'),
                    'C': pd.Series(1, index=list(range(5)), dtype='float32'),
                    'D': np.array([3] * 5, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train", "test"]),
                    'F': 'foo',
                    'G': ["yao", "lei", "li", "bai", "hello"]})
print("df3:\n{}".format(df3))
print("df3.columns {}\ndf3.index {}".format(df3.columns, df3.index))

# loc通过行和列的索引访问数据
# iloc通过行和列的下标访问数据
print("-----------------\n")
print("df3 index 0-1 on column b:\n{}".format(df3.loc[[0, 1], ["B"]]))
print("df3 index 0-1 on column b:\n{}".format(df3.loc[[0, 1], "B"]))  # 和前一条的区别是没有列名
print("df3 index 2-3 on column c e f:\n{}".format(df3.iloc[[2, 3], [2, 4, 5]]))
print("df3 index 2-3 on column e:\n{}".format(df3.iloc[[2, 3], [4]]))
print("df3 index 2-3 on column e:\n{}".format(df3.iloc[[2, 3], 4]))  # 和前一条的区别是没有列名
print("df3 index 2 on column e f:\n{}".format(df3.iloc[2, [4, 5]]))  # 没有索引
print("-----------------\n")

# 每个Series为一行
tseries1 = pd.Series(["C", "D", "E", "F", "G", "A", "B"])
tseries2 = pd.Series(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
df4 = pd.DataFrame([tseries1, tseries2])
print("df4:\n{}".format(df4))
print("df4.columns {}\ndf4.index {}".format(df4.columns, df4.index))

df5 = pd.DataFrame([[1, np.nan, 3], [4, 5, np.nan]])
print("df5:\n{}".format(df5))
print("df5.columns {}\ndf5.index {}".format(df5.columns, df5.index))

print("-----------------\n")
from math import isnan

t1 = np.nan
print("isnan {} value {} type {}".format(isnan(t1), t1, type(t1)))

# http://python.jobbole.com/89084/?utm_source=top.jobbole.com&utm_medium=relatedArticles
# http://python.jobbole.com/89331/?utm_source=blog.jobbole.com&utm_medium=relatedPosts
# http://python.jobbole.com/89081/?utm_source=blog.jobbole.com&utm_medium=relatedPosts