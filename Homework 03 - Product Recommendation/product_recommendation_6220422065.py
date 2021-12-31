# -*- coding: utf-8 -*-
"""Product Recommendation-6220422065.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tfAQKxrlZMeuEPyzFAEMEhrlEDfqzQEj

# Import Libraries

# Suthasinee Pojam 6220422065
"""

!pip install networkx
!wget https://awards.opdc.go.th/awards_opdc/assets/fonts/THSarabunNew/THSarabunNew.ttf
!wget -q http://www.arts.chula.ac.th/ling/wp-content/uploads/TH-Sarabun_Chula1.1.zip -O font.zip
!unzip -qj font.zip TH-Sarabun_Chula1.1/THSarabunChula-Regular.ttf
!apt install fonts-thai-tlwg

import numpy as np
import pandas as pd
import glob
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rcParams
import seaborn  as sns
import numpy as np
from sklearn.metrics import jaccard_score

from scipy.spatial.distance import cosine
from matplotlib.pyplot import figure, text
import networkx as nx

# Set font
font_list = fm.createFontList(['THSarabunChula-Regular.ttf'])
print(font_list)
fm.fontManager.ttflist.extend(font_list)
# fm.fontManager.addfont(font_list)
plt.rcParams['font.family'] = 'TH Sarabun Chula'
plt.rcParams['xtick.labelsize'] = 20.0
plt.rcParams['ytick.labelsize'] = 20.0

# Find font path
print(matplotlib.matplotlib_fname())
# Find font cache path
print(matplotlib.get_cachedir())

from google.colab import drive
drive.mount("/content/drive")

"""# Import Dataset"""

df = pd.read_csv('/content/Customer Preference Survey (Responses) - Form Responses 1.csv')
print(df.shape)
df.head()

#EDA 
df.info()

df.isnull().sum()

"""# Data Cleansing

### Drop Missing Value
"""

obj = df.isnull().sum()
for key,value in obj.iteritems():
    if value >= 1:
        print(key,",",value)

df=df.replace(['ไม่เคย','ไม่เคยซือ','ไม่','ไม่เคยซื้อ'],0)
df=df.replace(['เคยซื้อ','เคย'],1)
df['Transaction_id'] = [i for i in range(1,(df.shape[0]+1))]

df[['playstation5','เครื่องทำขนมปัง','Ergonomic Wrist Rest','เครื่องอบผ้า','เครื่องชงกาแฟแคปซูล','เก้าอี้ LA-Z-Boy','เครื่องให้อาหารสัตว์อัตโนมัติ','บัตตาเลี่ยน','แก้วเก็บความเย็น','ลู่วิ่งออกกำลังกาย','Kindle','เครื่องซักผ้า','Bluetooth Speaker','ห้องน้ำแมวอัตโนมัติ','PS5','ทรายแมว','ลำโพง pixel','Logitech Mx Master 3 Mouse','ตุ๊กตา ty','น้ำพุแมว','Robot ดูดฝุ่น','Mechanical keyboard','Nintendo switch','หนังสือ python','gaming chair','Deskmat','Dew - ไฟโรเซ่','เทียนหอม jo malone','กระติกน้ำ 2 ลิตร','ที่นอน memory form','พลาสเตอร์บรรเทาปวด ตราเสือ','การ์ดจอ RTX 3080','ขนมจีนน้ำยาปู','Salmon Sashimi','จักรยานเสือหมอบ','ไฟแต่งห้องมินิมอล','External Harddisk','หม้อทอดไร้น้ํามัน','airpods ','ยาดม','ไฟส่องหน้าไลฟ์สด']]\
=df[['playstation5','เครื่องทำขนมปัง','Ergonomic Wrist Rest','เครื่องอบผ้า','เครื่องชงกาแฟแคปซูล','เก้าอี้ LA-Z-Boy','เครื่องให้อาหารสัตว์อัตโนมัติ','บัตตาเลี่ยน','แก้วเก็บความเย็น','ลู่วิ่งออกกำลังกาย','Kindle','เครื่องซักผ้า','Bluetooth Speaker','ห้องน้ำแมวอัตโนมัติ','PS5','ทรายแมว','ลำโพง pixel','Logitech Mx Master 3 Mouse','ตุ๊กตา ty','น้ำพุแมว','Robot ดูดฝุ่น','Mechanical keyboard','Nintendo switch','หนังสือ python','gaming chair','Deskmat','Dew - ไฟโรเซ่','เทียนหอม jo malone','กระติกน้ำ 2 ลิตร','ที่นอน memory form','พลาสเตอร์บรรเทาปวด ตราเสือ','การ์ดจอ RTX 3080','ขนมจีนน้ำยาปู','Salmon Sashimi','จักรยานเสือหมอบ','ไฟแต่งห้องมินิมอล','External Harddisk','หม้อทอดไร้น้ํามัน','airpods ','ยาดม','ไฟส่องหน้าไลฟ์สด']]\
.fillna( value = df[['playstation5','เครื่องทำขนมปัง','Ergonomic Wrist Rest','เครื่องอบผ้า','เครื่องชงกาแฟแคปซูล','เก้าอี้ LA-Z-Boy','เครื่องให้อาหารสัตว์อัตโนมัติ','บัตตาเลี่ยน','แก้วเก็บความเย็น','ลู่วิ่งออกกำลังกาย','Kindle','เครื่องซักผ้า','Bluetooth Speaker','ห้องน้ำแมวอัตโนมัติ','PS5','ทรายแมว','ลำโพง pixel','Logitech Mx Master 3 Mouse','ตุ๊กตา ty','น้ำพุแมว','Robot ดูดฝุ่น','Mechanical keyboard','Nintendo switch','หนังสือ python','gaming chair','Deskmat','Dew - ไฟโรเซ่','เทียนหอม jo malone','กระติกน้ำ 2 ลิตร','ที่นอน memory form','พลาสเตอร์บรรเทาปวด ตราเสือ','การ์ดจอ RTX 3080','ขนมจีนน้ำยาปู','Salmon Sashimi','จักรยานเสือหมอบ','ไฟแต่งห้องมินิมอล','External Harddisk','หม้อทอดไร้น้ํามัน','airpods ','ยาดม','ไฟส่องหน้าไลฟ์สด']]\
.median())
df.tail()

df.iloc[:,2].value_counts()

"""# Data Preparation"""

df_data = df.iloc[:,2:-1]
df_data

"""#Visualization"""

figure, axes = plt.subplots(2, 1,figsize=(20,30))
df_data.sum().plot.hist(bins= 20,color = '#ffbb00' ,ax=axes[0],title= 'Item Distribution')
df_data.sum().sort_values(ascending= True).tail(10).plot.barh(color = '#aadddd' ,ax=axes[1],title='Top10 Common Purchase/Use')
 
plt.show('Distribution')

df.describe().T.sort_values('mean',ascending = False)

item_item_matrix = pd.DataFrame(index=df.columns,columns=df.columns)
item_item_matrix1 = item_item_matrix.iloc[2:-1,2:-1]

"""#ITEM-ITEM Collaborative filtering"""

for i in range(0,len(item_item_matrix1.columns)) :
    # Loop through the columns for each column
    for j in range(0,len(item_item_matrix1.columns)) :
      # Fill in placeholder with cosine similarities
      item_item_matrix1.iloc[i,j] =  1-cosine(df_data.iloc[:,i],df_data.iloc[:,j])

item_item_matrix1.head(10)

"""#ITEM-ITEM Heat Map"""

corr = np.round(np.array(item_item_matrix1).astype(float),decimals=2)
corr

mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = False
plt.figure(figsize=(20,15))
with sns.axes_style("white"):
    ax = sns.heatmap(corr, mask=mask, vmin=0,vmax=.9, square=True, annot=True, cbar=False,  linewidths=.2)
    plt.show()

item_item_matrix1 = item_item_matrix1.dropna()

links = item_item_matrix.rename_axis('related item', 
                                     axis='columns').stack().reset_index()
links.columns = ['item', 'related item','value']

links['value'] = links.value.apply( lambda x :  round(x,3))
links.head(10)

links= links.loc[(links['item'] !=links['related item'])].sort_values('value',ascending = False)
links_filtered=links.loc[(links['item'] != links['related item'])& (links['value'] > 0.75)]
links_filtered.shape

links_filtered.sort_values(by = ['value'], ascending = False).head(10)

fig, ax = plt.subplots(figsize=(25,18))

GA=nx.from_pandas_edgelist(links_filtered,source='item',target='related item',edge_attr=['value'])

weight2 = [ float(i['value']) for i in dict(GA.edges).values()] 
weight2 = ((np.array(weight2)- min(weight2))/(max(weight2)-min(weight2)))*5
labels2 = [i for i in dict(GA.nodes)]
labels2 = {i:i for i in dict(GA.nodes).keys()}

pos = nx.spring_layout(GA,weight='weight2',  k=12)
nx.draw_networkx_nodes(GA, pos,ax = ax,node_color = 'yellow') 
nx.draw_networkx_edges(GA, pos,edge_color='green',arrowsize=10, width=weight2, ax=ax ) 
edge_labels = nx.get_edge_attributes(GA, 'value')

nx.draw_networkx_edge_labels(GA, pos, edge_labels=edge_labels, font_color='red', font_size=18)
_ = nx.draw_networkx_labels(GA, pos, labels2, ax=ax, font_family='TH Sarabun Chula', font_size=25)
plt.show()

"""#USER-USER Collaborative filtering"""

df.columns

df_uu = df.drop(['Timestamp','Transaction_id'],axis=1)
df_uu

from sklearn.metrics.pairwise import cosine_similarity

filtering_cosim = cosine_similarity(df_uu, df_uu)
print(filtering_cosim)

"""#USER-USER Heat Map"""

mask = np.zeros_like(filtering_cosim)
mask[np.triu_indices_from(mask)] = False
plt.figure(figsize=(20,15))
with sns.axes_style("white"):
    ax = sns.heatmap(filtering_cosim, mask=mask, vmin=0, vmax=1, square=True,  cmap="YlGnBu", annot=True, linewidths=.5, cbar=False)
    plt.show()

index_user = 0 # user001
most_sim_users = sorted(list(enumerate(filtering_cosim[index_user])), key=lambda x: x[1], reverse=True)
most_sim_users = most_sim_users[1:6]
sim_users = [x[0] for x in most_sim_users]
print(f'similarity user001 : {sim_users}')

sim_users

df.head()

list_users = []
for u in sim_users:
    list_users.append(df.iloc[u,0])
list_users

df_sim_u = df_uu.iloc[sim_users, :]
df_sim_u

mean_score = pd.Series(df_sim_u.mean(axis=0))
mean_score = mean_score.sort_values(axis=0, ascending=False)
mean_score

recom = list(mean_score.iloc[0:10].keys())
for i in recom:
    print("แนะนำ {} ให้กับ {}".format(i,list_users))
