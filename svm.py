# -*- coding:cp936 -*-
import time
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.cross_validation import train_test_split
#import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, fbeta_score
#1.准备数据
data = np.loadtxt('bad_good.txt', dtype=np.float, delimiter=',')
x, y = np.split(data, (-1, ), axis=1)
#2.训练数据与测试数据分开
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.5)

#3.用于分类的各种核函数
'''clf_linear  = svm.SVC(kernel='linear').fit(x, y)
#clf_linear  = svm.LinearSVC().fit(x, y)
clf_poly    = svm.SVC(kernel='poly', degree=3).fit(x, y)
#clf_rbf     = svm.SVC().fit(x, y)
clf_sigmoid = svm.SVC(kernel='sigmoid').fit(x, y)

'''
#default setup:
time0 = time.time()
#clf = svm.SVC().fit(x, y)
#clf = svm.SVC(kernel='sigmoid').fit(x, y)

#clf  = svm.SVC(kernel='poly', degree=3).fit(x, y)
#clf = svm.SVC(kernel='linear').fit(x, y)


#clf= svm.SVC(C=1, kernel='rbf', gamma=0.001,class_weight={-1: 1, 1: 1}).fit(x,y)
clf = svm.SVC(C=1, kernel='rbf', gamma=0.5, class_weight={-1: 1.5, 1: 1}).fit(x,y)#C=1,C=0.8,C=2,gamma = 0.001,0.5,1
y_hat = clf.predict(x_test)
time1 = time.time()
print u'正确率：\t', accuracy_score(y_test, y_hat)
print u' 精度 ：\t', precision_score(y_test, y_hat)
print u'召回率：\t', recall_score(y_test, y_hat)
print u'F1Score：\t', f1_score(y_test, y_hat)
print u'时间：\t',time1-time0,u'秒'
