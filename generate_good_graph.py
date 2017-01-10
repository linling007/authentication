import pandas as pd
import networkx as nx
#import matplotlib.pyplot as plt
import os
f = open('good.txt','w+')#######1.改这里
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
	f0 = len(set(data[3]))#使用的计算机的数量
	f1 = len(set(data[4]))#认证过的计算机的数量

	f2 = len(G.nodes())#图中节点的个数，去除重复f2 = f0+f1？
	f3 = len(G.edges())#图中边的个数，去除重复

	f5 = nx.degree_histogram(G)[1]#节点度数为1   #孤立节点的个数
	f6 = len(nx.degree_histogram(G))-1#节点度数最大为几


	f7 = nx.number_connected_components(G)#连通组件的个数


	f8 = nx.average_clustering(G)#平均聚类系数
	f9 = nx.average_node_connectivity(G)#节点的平均连通性
	f10 = nx.density(G)#图密度
	#--------------------------------------------------------

	G = max(nx.connected_component_subgraphs(G), key=len)
	#G = max(nx.connected_components(G), key=len)#
	f11 = nx.average_shortest_path_length(G)#返回图G所有节点间平均最短路径长度。
	f12 = nx.diameter(G)#返回图G的直径（最长最短路径的长度）
	f13 = nx.radius(G)#半径

	#f11 = nx.degree_centrality(G)#度中心性
	#f12 = nx.betweenness_centrality(G)#介数中心性


	f14 = nx.degree_assortativity_coefficient(G)#调用 nx.degree_assortativity(G) 方法可以计算一个图的度匹配性。（同配性）
	#L = [f0,f1,f2,f3,f4,f5,f6]
	#L = [f0,f1,f2,f3,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,-1]#
	return [f0,f1,f2,f3,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,1]####修改这里，最后
	
	
fnameL = []#将文件名放到一个列表里
for fname in os.listdir('gooduserss/'):#2.改这里
	fnameL.append(fname)

for i in fnameL:#对于每一个文件提取属性，放到bad.txt里面。
	print i#看进度
	#str(generate(i)).strip('[')#有待验证！
	print >> f,str(generate(i)).strip(']')
	
f.close()


#*******************show the figure*********************
#nx.draw(G,node_size = 3,with_labels = True)
#plt.grid(False)
#plt.show()
#*******************show the figure*********************

