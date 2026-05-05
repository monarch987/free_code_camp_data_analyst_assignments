import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import calendar
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)


df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'])



df = df[(df['value']>=df['value'].quantile(0.025)) & (df['value']<=df['value'].quantile(0.975))            
    ]


def new_df():

    df_new = df.copy()


    df_new['year'] = df['date'].dt.year

    df_new['month'] = df['date'].dt.month

    df_new['day'] = df['date'].dt.day

    df_new.set_index('date',inplace=True)

    return df_new


def draw_line_plot():
    # Draw line plot

    fig,ax = plt.subplots()

    ax.plot(df.index,df['value'])
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_ylabel('Page Views')
    ax.set_xlabel('Date')
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot

    months = ['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']

    #numerical-->month
    month_order = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 
                    7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    
    def numeric_to_month(x):

        mnth = month_order[x]
        return str(mnth)

    df_bar = new_df()

    df_bar = df_bar.groupby(['year','month'])['value'].mean().reset_index()
    

    df_bar['month'] = df_bar['month'].apply(lambda x:numeric_to_month(x))

    # Draw bar plot

    fig,axes = plt.subplots()
    
    sns.barplot(x='year',y='value',hue='month',hue_order=months,data= df_bar,ax=axes)

    axes.set_xlabel('Years')
    axes.set_ylabel('Average Page Views')   

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():

    #numerical-->month
    month_order = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 
               7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}

    def numeric_to_month(x):

        x= int(x)
        mnth = month_order[x]
        return str(mnth)


    # Prepare data for box plots (this part is done!)

    df_box = new_df()

    df_box = df_box.sort_values(by='month',ascending=True) 

    df_box['month'] = df_box['month'].apply(lambda x:numeric_to_month(x))
    
    # Draw box plots (using Seaborn)
    
    fig, axes = plt.subplots(1, 2)

    sns.boxplot(x='year',y='value',data=df_box,ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')

    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    

    sns.boxplot(x='month',y='value',data=df_box,ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')

    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig




if __name__ == '__main__':

    pass
    draw_bar_plot()
