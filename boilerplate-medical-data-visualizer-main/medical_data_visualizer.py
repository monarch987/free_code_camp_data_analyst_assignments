import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = None

# 3
def is_overweight(row):
    
    w = row['weight']
    h = row['height']
     
    if h==0 or pd.isna(h) or pd.isna(w):
        return 0

    h = h/100 #since height s in cm converting it to meter
    
    bmi = (w/h**2)
   
    if bmi>25 : 
        return 1 
    elif bmi <=25: 
        return 0
    
def normalize_values(x):
    
    if x <=1:
        return 0
    
    elif x >1:
        return 1
    
#inserting value along column hence axis=1
df['overweight'] = df.apply(is_overweight,axis=1)

### NORMALIZE GLUCOSE & CHOLESTROL VALUES so unfiormity is present in data to be rendered

df['gluc'] = df['gluc'].apply(normalize_values)
df['cholesterol'] = df['cholesterol'].apply(normalize_values)


# print(df_cat.head(10))
# print(df.columns)

#
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars='cardio',value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],var_name='variable')


    df_cat = df_cat.groupby(['cardio','variable','value']).size().reset_index(name='total')


    fig = sns.catplot(data=df_cat,x='variable',y='total',hue='value',col="cardio",kind='bar')
    
    fig.set_axis_labels('variable','total')
    fig = fig.fig
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():

    # 11
    df_heat = df[(df['ap_lo']<=df['ap_hi'])&
    (df['height']>=df['height'].quantile(0.025))&
    (df['height']<=df['height'].quantile(0.975))&
    (df['weight']>=df['weight'].quantile(0.025))&
    (df['weight']<=df['weight'].quantile(0.975))]


    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr,dtype=bool))

    # 14
    fig,ax = plt.subplots(figsize=(15,10)) 
    sns.heatmap(corr,mask=mask,fmt='.1f',annot=True,ax=ax)

    # 15

    # 16
    fig.savefig('heatmap.png')
    return fig


if __name__ == '__main__':

    # draw_cat_plot()
    # draw_heat_map()
    pass