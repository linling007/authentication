#coding:utf-8
from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

data = pd.read_csv('bad_good.txt',header = None)

import numpy as np
#print data
# bad_component = list(data[6])[:94]
# good_component = list(data[6])[94:]
# density = list(data[9])
#******************************
# bad_density = density[:94]
# good_density = density[94:]


isolate = list(data[4])
bad_isolate = isolate[:94]
good_isolate = isolate[94:]
#***************************
bad = bad_isolate
good = good_isolate
print bad,'\n',good
bad_L = [0]*5
good_L = [0]*5
for i in bad:
    if i >20:
        bad_L[4]+=1
    elif i>15:
        bad_L[3]+=1
    elif i>10:
        bad_L[2]+=1
    elif i>5:
        bad_L[1]+=1
    else:
        bad_L[0]+=1

for i in good:
    if i > 20:
        good_L[4] += 1
    elif i>15:
        good_L[3] += 1
    elif i > 10:
        good_L[2] += 1
    elif i > 5:
        good_L[1] += 1
    else :
        good_L[0] += 1
bad_result = [0.0]*5
j = 0
for i in bad_L:
    bad_result[j] = i/sum(bad_L)
    j+=1
good_result = [0.0]*5
j = 0
for i in good_L:
    good_result[j] = i/sum(good_L)
    j+=1
print bad_result, good_result


mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = [u'SimHei']
fig= plt.figure()
print u'中文测试'
plt.bar([0,5,10,15,20],bad_result,width = .5,color = 'r',alpha = 1,label = u'异常用户')
plt.bar([0.5,5.5,10.5,15.5,20.5],good_result,width =0.5,color = 'g',alpha = 1,label = u'正常用户' )
#plt.title('Isolate authentication distribution')
plt.title(u'孤立认证分布')
plt.xlabel(u'次数')
plt.ylabel(u'频率')
plt.legend(loc = 'best')
#plt.hist(bad_component_L,normed = 1)
plt.show()
# print bad_density,good_density
# print bad_isolate,good_isolate