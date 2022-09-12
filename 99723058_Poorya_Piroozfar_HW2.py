#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
df=pd.read_csv("F:\\IUST\\ترم 2\\داده کاوی\\DataMining_HW2\\500000FamilySample-990402\\500000FamilySample-990402.csv")


# # Question 1.1

# In[12]:


cf=df[['CountyName','Daramad_Total_Rials']]
cf1=cf.groupby('CountyName').mean()
cf1.rename(columns={'Daramad_Total_Rials':'Daramad_mean_Rials'},inplace=True)
cf1


# # Question 1.2

# In[16]:


pf=df[['IsBimarkhas','IsBehzisti_Malool','CountyName','ProvinceName']]
pf1=pf.loc[pf.ProvinceName == 'تهران']
pf1.loc[pf1.IsBimarkhas == 1]
pf2 = pf1.groupby(['IsBehzisti_Malool','CountyName']).sum()
pf3=pf2[['IsBimarkhas']]
pf3.rename(columns={'IsBimarkhas':'Count_Bimarkhas'},inplace=True)
pf3.unstack()


# # Question 1.3

# In[58]:


gf=df[['ProvinceName','CountyName','SenfName','BirthDate','IsUrban']]
nf = df.loc[df.ProvinceName == 'مازندران']
nf2 = nf.loc[nf.IsUrban == 1]
nf2['Year']=pd.DatetimeIndex(nf2['BirthDate']).year
nf3 = nf2.groupby(['CountyName' , 'Year']).count()
nf3.rename(columns={'SenfName':'Count_Senf'},inplace=True)
nf4=nf3[['Count_Senf']]

nf4
#nf4.unstack()


# # Question 1.4

# In[4]:


lf1=df[['Variz95','Variz96','Variz97', 'ProvinceName' , 'Gender', 'IsUrban']]
lf1.groupby(['ProvinceName' , 'IsUrban', 'Gender']).sum()


# In[17]:


kf1=df[['Variz95' , 'ProvinceName' , 'Gender', 'IsUrban']]
kf2 = kf1.groupby(['ProvinceName' , 'IsUrban', 'Gender']).sum()
kf2.unstack()


# In[11]:


kf3=df[['Variz96' , 'ProvinceName' , 'Gender', 'IsUrban']]
kf4 = kf3.groupby(['ProvinceName' , 'IsUrban', 'Gender']).sum()
kf4.unstack()


# In[12]:


kf5=df[['Variz97' , 'ProvinceName' , 'Gender', 'IsUrban']]
kf6 = kf5.groupby(['ProvinceName' , 'IsUrban', 'Gender']).sum()
kf6.unstack()


# # Question 1.5

# In[32]:


qf = pd.DataFrame(df , columns=['Id' ,'ParentId' , 'CountyName' , 'Cars_Count', 'CarPrice_Sum'])
qf['mean_car'] = qf['CarPrice_Sum'] / qf['Cars_Count']

qf1 = qf.groupby([ 'CountyName' ,'ParentId']).count()
qf2 = qf1[['Id']]

qf3 = qf.groupby([ 'CountyName' ,'ParentId']).sum()
qf4 = qf3[['mean_car']]

qf5 = pd.merge(qf2, qf4, on=["CountyName", "ParentId"])
qf5['mean_all'] = qf5['mean_car'] / qf5['Id']
qf5.pop('mean_car')
qf5.rename(columns={'Id':'Count_family members'},inplace=True)

qf6=qf5.groupby([ 'CountyName','Count_family members']).mean()
qf6

#qf5.unstack()


# # Question 2.1

# In[33]:


wf=df[['Gender','Card9801','Card9802','Card9803','Card9804','Card9805','Card9806']]
wf1=wf.groupby('Gender').sum()
wf1


# # Question 2.2

# In[43]:


uf=df[['Id','Gender','ProvinceName','Daramad_Total_Rials','IsBazneshaste_Sandoghha','IsBimarkhas']]
uf1 = uf.loc[uf.IsBazneshaste_Sandoghha == 1]
uf2 = uf1.loc[uf1.IsBimarkhas == 1]
uf3=uf2.groupby(['ProvinceName','Gender']).mean()
uf3.rename(columns={'Daramad_Total_Rials':'Mean_Daramad'},inplace=True)
uf4=uf3[['Mean_Daramad']]
uf4.unstack()


# # Question 2.3

# In[45]:


ef=df[['Id','ProvinceName','Gender','Trip_AirNonPilgrimageCount_95','Trip_AirNonPilgrimageCount_96','Trip_AirNonPilgrimageCount_97','Trip_AirNonPilgrimageCount_98']]

ef1=ef.groupby(['ProvinceName','Gender']).sum()
ef1.pop('Id')
ef1


# # Question 2.4

# In[30]:


yf=df[['Id','ProvinceName','IsUrban','Bardasht95','Bardasht96','Bardasht97']]
yf1=yf.groupby(['ProvinceName','IsUrban']).sum()
yf1.pop('Id')
yf1


# # Question 2.5

# In[57]:


zf=df[['ProvinceName','IsUrban','IsTamin_Karfarma','Tamin_KargarCount']]
zf1 = zf.loc[zf.IsTamin_Karfarma == 1]
zf1=zf.groupby(['ProvinceName','IsUrban']).sum()
zf1.pop('IsTamin_Karfarma')
zf1.unstack()


# In[ ]:




