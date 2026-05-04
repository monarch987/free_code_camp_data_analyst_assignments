import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = np.array(df['Year'])
    y = np.array(df['CSIRO Adjusted Sea Level'])

    # Create scatter plot
    plt.scatter(x,y)
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    # plt.show()

    #finding slope and intercept of the best fit line using linregress 
    slope,intercept, r_value, p_value, std_err = linregress(x,y)
    
    # Create first line of best fit

    x_pred = np.arange(df['Year'].min(),2051,1)
    y_pred = slope*x_pred+intercept
    plt.scatter(x_pred,y_pred)
    plt.plot(x_pred,y_pred,color='red')
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    # plt.show()

    # Create second line of best fit

    twentith_cent_df = df[df['Year']>=2000]
    new_slope,new_intercept, r_value, p_value, std_err = linregress(twentith_cent_df['Year'], twentith_cent_df['CSIRO Adjusted Sea Level'])
    
    pred_x = np.arange(2000,2051,1)
    pred_y = new_slope*pred_x + new_intercept

    plt.scatter(pred_x,pred_y)
    plt.plot(pred_x,pred_y,color='red')
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    # plt.show()

    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()