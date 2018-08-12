
# coding: utf-8

# In[1]:


# get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np


# In[2]:


#导入股票数据,把日期列作为索引
data = pd.read_csv('yahoo-data/600690.csv',index_col='Date',parse_dates=True)
data


# In[3]:


#从1993年到2016年,可以看到有5847条数据
#提取Adj Close(收盤價)那一列数据
adj_price = data['Adj Close']
adj_price


# In[4]:


#把数据用月份重新采样
#这个ohlc对应的是股市中的open，high，low，close这几个价格
# resampled = adj_price.resample('m',how='ohlc')  #py2写法
resampled = adj_price.resample('m').ohlc()    #py3写法
resampled


# In[5]:


#计算股票每月的波动幅度
#一个股票波动幅度较大的话,可以获得的投机收益也会比较大,当然同时风险也是比较大
(resampled.high - resampled.low) / resampled.low


# In[6]:


#计算每个月的波动幅度的平均值
ripple = (resampled.high - resampled.low ) / resampled.low
ripple.mean()


# In[7]:


#用图形化展示该股票的每月波动
adj_price.plot(figsize=(8,6))


# In[8]:


#该股票2016-1996之间最高价与最低价之间差距多少倍
#即假设在1996-2016年之间,投资者从最低点买入,从最高点卖出,投资收益1112倍,当然实际是不闲时的
(adj_price.max() - adj_price.min())/adj_price.min()


# In[9]:


#假设投资者从该股票一上市就买入,至今未抛出,查看收益倍数
adj_price.iloc[0]/adj_price.iloc[-1]


# In[14]:


#计算年平均增长幅度
total_growth = adj_price.iloc[0]/adj_price.iloc[-1]
new_date = adj_price.index[0].year
old_date = adj_price.index[-1].year
new_date,old_date
total_growth ** (1/(new_date - old_date))


# In[16]:


#查看每年的情况
adj_price.to_period('A').groupby(level=0).first()


# In[17]:


price_in_year = adj_price.to_period('A').groupby(level=0).first()
price_in_year.plot()


# In[18]:


diff = price_in_year.diff()
diff


# In[19]:


#每年的增长率
rate = diff / (price_in_year-diff)


# In[20]:


rate


# In[21]:


rate.plot(kind = 'bar')

