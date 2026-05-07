import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    
    df = pd.read_csv('adult_data.csv')


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    # race_count = None
    race_count = df.groupby('race').size()

    # What is the average age of men?
    # average_age_men = None
    avg_age = df.groupby('sex')['age'].mean()
    average_age_men = round(avg_age.loc['Male'],1)

    # What is the percentage of people who have a Bachelor's degree?
    educated_populus = df.groupby('education').size()

    percentage_bachelors = round((educated_populus.loc['Bachelors']/educated_populus.sum())*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    
    high_pay_crowd = df.groupby(['education','salary']).size().reset_index(name='count')


    high_pay_crowd = ((high_pay_crowd[high_pay_crowd['salary'] == '>50K']).drop('salary',axis=1)).set_index('education') 

    bachelors_50_K  = high_pay_crowd.loc['Bachelors','count']

    masters_50_K  = high_pay_crowd.loc['Masters','count']

    doctorates_50_K  = high_pay_crowd.loc['Doctorate','count']

    other_50_K = (high_pay_crowd['count'].sum()) - (bachelors_50_K + masters_50_K + doctorates_50_K)
    # print(other_50_K)
 

    total_highly_educated = educated_populus.loc['Bachelors']+educated_populus.loc['Masters']+educated_populus.loc['Doctorate']
    total_lower_educated = educated_populus.sum() - total_highly_educated
    
    percent_b = (bachelors_50_K/total_highly_educated)*100
    percent_m = (masters_50_K/total_highly_educated)*100
    percent_d = (doctorates_50_K/total_highly_educated)*100

    perecentage_advanced = round((percent_b+percent_m+percent_d),1)
        
    # What percentage of people without advanced education make more than 50K?
    perecentage_non_advanced = round((other_50_K/total_lower_educated)*100,1)

    # print(perecentage_advanced,perecentage_non_advanced)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # higher_education = (bachelors_50_K+masters_50_K+doctorates_50_K)
    # lower_education = total- (bachelors_50_K+masters_50_K+doctorates_50_K)

    # percentage with salary >50K
    higher_education_rich = perecentage_advanced
    lower_education_rich = perecentage_non_advanced

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    
    salaried_greater_than_50k_work_min_hrs = df[(df['salary']=='>50K') & (df['hours-per-week']==min_work_hours)]

    total_people_work_min_hrs =  df[df['hours-per-week'] == min_work_hours]
    
    rich_percentage = round((salaried_greater_than_50k_work_min_hrs['hours-per-week'].count()/total_people_work_min_hrs['hours-per-week'].count())*100,1)

    # print("rich_percentage",rich_percentage)

    # What country has the highest percentage of people that earn >50K?

    max_earning_per_country =  (df[df['salary']=='>50K']).groupby('native-country').size()
    
    earning_per_country = (df.groupby('native-country')).size()

    earning_country_df = pd.concat([max_earning_per_country,earning_per_country],axis=1)

    earning_country_df['max_earning_percent'] = round((max_earning_per_country/earning_per_country)*100,1)


    highest_earning_country_percentage = earning_country_df['max_earning_percent'].max()


    earning_country_df = (earning_country_df.reset_index()).set_index('max_earning_percent')

    highest_earning_country = earning_country_df.loc[highest_earning_country_percentage,'native-country']


    # Identify the most popular occupation for those who earn >50K in India.

    #forms required dataframe    
    indian_populus_50K = df[(df['native-country']=='India') & (df['salary']=='>50K')]

    #reset_index brigs datagroupframe in dataframe ,we rename nameless column as 'count' which holds summation of each group 
    indian_populus_50K = indian_populus_50K.groupby('occupation').size().reset_index(name='count')


    count_of_most_prefered_occupation = indian_populus_50K['count'].max()

    #resetting index so we can access occupation based of max count we have      
    indian_populus_50K = (indian_populus_50K.reset_index()).set_index('count')

    top_IN_occupation = indian_populus_50K.loc[count_of_most_prefered_occupation ,'occupation']

    # print(top_IN_occupation)


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }



if __name__ == '__main__':
    calculate_demographic_data()    