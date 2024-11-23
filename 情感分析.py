from snownlp import SnowNLP
import pandas as pd
import numpy as np
from collections import defaultdict
import os
import re
import jieba
import codecs
import seaborn as sns
import matplotlib.pyplot as plt
# 评论情感分析
# f = open('earphone_sentiment.csv',encoding='gbk') 
# line = f.readline()
data=pd.read_excel("D:\\美赛第一次模拟\\MCM_Problem_C_Data\\pacifier.xlsx").astype(str) #字符类型
# data.head()

with open("D:\美赛第一次模拟\stop_word.txt",'r',encoding='utf-8') as f:
    stopwords=set([line.replace('\n','')for line in f])
f.close() 
sum=0
count=0
for i in range(len(data['review_body'])):
    line=jieba.cut(data.loc[i,'review_body'])           #分词
    words=''
    for seg in line:
        if seg not in stopwords and seg!=" ":        #文本清洗
            words=words+seg+' '
    if len(words)!=0:
        # print(words)        #输出每一段评论的情感得分
        d=SnowNLP(words)
        # print('{}'.format(d.sentiments))
        data.loc[i,'sentiment_score']=float(d.sentiments)     #原数据框中增加情感得分列
        sum+=d.sentiments
        count+=1
score=sum/count
# print('finalscore={}'.format(score))    #输出最终情感得分

#情感值以方法一计算的作为值
#获取同一列中不重复的值
a=list(data['review_body'].unique())
sum_scores=dict()
#求对应主题的情感均值
for r in range(len(a)):
    de=data.loc[data['review_body']==a[r]]
    sum_scores[a[r]]=round(de['sentiment_score'].mean(),2)
print(sum_scores)


# # 这两行代码解决 plt 中文显示的问题
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# #数据可视化
# sns.barplot(x=list(sum_scores.values()),y=list(sum_scores.keys()))
# plt.xlabel('情感值')
# plt.ylabel('主题')
# plt.title('不同主题下的情感得分柱形图')
# for x,y in enumerate(list(sum_scores.values())):
#     plt.text(y,x,'%s'%y,va='center')
# plt.show()