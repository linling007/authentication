import pandas as pd
import numpy as np
import time
print time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime(time.time()))
print "The code is running,please don't bother or close it"
#badguys = ['U1164', 'U1600', 'U114', 'U8170', 'U293', 'U2758', 'U3406', 'U212', 'U748', 'U524', 'U9763', 'U218', 'U374', 'U1519', 'U1048', 'U1592', 'U288', 'U162', 'U8946', 'U7004', 'U1289', 'U995', 'U207', 'U3575', 'U1569', 'U1106', 'U3005', 'U1581', 'U3764', 'U3486', 'U9947', 'U2575', 'U4112', 'U1450', 'U4353', 'U415', 'U250', 'U1025', 'U7594', 'U314', 'U24', 'U20', 'U4448', 'U1133', 'U3718', 'U9407', 'U2837', 'U679', 'U8601', 'U3905', 'U6691', 'U795', 'U1480', 'U7507', 'U1723', 'U13', 'U12', 'U5087', 'U3549', 'U10379', 'U4978', 'U7375', 'U1653', 'U3206', 'U86', 'U5254', 'U6764', 'U655', 'U3635', 'U6572', 'U7761', 'U342', 'U636', 'U227', 'U349', 'U2231', 'U1145', 'U78', 'U3277', 'U882', 'U9263', 'U1506', 'U642', 'U8777', 'U1306', 'U825', 'U4856', 'U453', 'U620', 'U7394', 'U6115', 'U7311', 'U8840', 'U66', 'U1789', 'U737', 'U8168', 'U1467']
#length = 98
good = np.loadtxt('good_user2',dtype = str)
goodguys = list(good)

data = pd.read_csv('auth.txt',header = None,chunksize = 100000)
for i in range(79,len(goodguys)):
	f = []
	for chunk in data:
			f = chunk[chunk[1] == goodguys[i]+'@DOM1']
			#if chunk.ix[j,1].split('@')[0] == badguys[i]:	
			f.to_csv('goodusers/goodguys[%d]'%i,mode = 'a',header = False,index = False)
	data = pd.read_csv('auth.txt',header = None,chunksize = 100000)

print time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime(time.time()))
print 'Happy New Year!'