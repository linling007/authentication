import pandas as pd
import networkx as nx
#import matplotlib.pyplot as plt
import os
f = open('good.txt','w+')#######1.������
def generate(User):
	G = nx.Graph()
	User = User
	#User = 'badguys[0]'
	df  = pd.read_csv(User,header = None,chunksize = 100000)
	for data in df:
		for i in range(len(data)):
			if data.ix[i,3] != data.ix[i,4]:
				G.add_edges_from([(data.ix[i,3],data.ix[i,4])])
	#nx.write_adjlist(G,'G_adjlist')
	f0 = len(set(data[3]))#ʹ�õļ����������
	f1 = len(set(data[4]))#��֤���ļ����������

	f2 = len(G.nodes())#ͼ�нڵ�ĸ�����ȥ���ظ�f2 = f0+f1��
	f3 = len(G.edges())#ͼ�бߵĸ�����ȥ���ظ�

	f5 = nx.degree_histogram(G)[1]#�ڵ����Ϊ1   #�����ڵ�ĸ���
	f6 = len(nx.degree_histogram(G))-1#�ڵ�������Ϊ��


	f7 = nx.number_connected_components(G)#��ͨ����ĸ���


	f8 = nx.average_clustering(G)#ƽ������ϵ��
	f9 = nx.average_node_connectivity(G)#�ڵ��ƽ����ͨ��
	f10 = nx.density(G)#ͼ�ܶ�
	#--------------------------------------------------------

	G = max(nx.connected_component_subgraphs(G), key=len)
	#G = max(nx.connected_components(G), key=len)#
	f11 = nx.average_shortest_path_length(G)#����ͼG���нڵ��ƽ�����·�����ȡ�
	f12 = nx.diameter(G)#����ͼG��ֱ��������·���ĳ��ȣ�
	f13 = nx.radius(G)#�뾶

	#f11 = nx.degree_centrality(G)#��������
	#f12 = nx.betweenness_centrality(G)#����������


	f14 = nx.degree_assortativity_coefficient(G)#���� nx.degree_assortativity(G) �������Լ���һ��ͼ�Ķ�ƥ���ԡ���ͬ���ԣ�
	#L = [f0,f1,f2,f3,f4,f5,f6]
	#L = [f0,f1,f2,f3,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,-1]#
	return [f0,f1,f2,f3,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,1]####�޸�������
	
	
fnameL = []#���ļ����ŵ�һ���б���
for fname in os.listdir('gooduserss/'):#2.������
	fnameL.append(fname)

for i in fnameL:#����ÿһ���ļ���ȡ���ԣ��ŵ�bad.txt���档
	print i#������
	#str(generate(i)).strip('[')#�д���֤��
	print >> f,str(generate(i)).strip(']')
	
f.close()


#*******************show the figure*********************
#nx.draw(G,node_size = 3,with_labels = True)
#plt.grid(False)
#plt.show()
#*******************show the figure*********************

