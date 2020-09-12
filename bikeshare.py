import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    x=0
    city=''
    while city not in ['chicago', 'new york city', 'washington']:
        if x==1:
            print('wrong input')
        city=input('Would you like to see data for chicago, new york city, washington name of the city to analyze : ')
        x=1


    # TO DO: get user input for month (all, january, february, ... , june)
    x=0
    months= ['January','February','March','April','May','June','July','August','September','October','November','December','all']
    month=''
    while month not in months:
        if x==1:
            print('wrong input')
        month=input('name of the month to filter by, or "all" to apply no month filter : ')
        if month !='all':
            month=month.capitalize()
        x=1


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    x=0
    days= ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','all']
    day=''
    while day not in days:
        if x==1:
            print('wrong input')
        day=input('name of the day of week to filter by, or "all" to apply no day filter : ')
        if day !='all':
            day=day.capitalize()
        x=1


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] =df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['','January','February','March','April','May','June','July','August','September','October','November','December']
        month = months.index(month)
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    

    # TO DO: display the most common month
    months = ['','January','February','March','April','May','June','July','August','September','October','November','December']
    popular_month = df['month'].value_counts().idxmax()
    print('Most Frequent month : ', months[popular_month])


    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].value_counts().idxmax()
    print('Most Frequent day of week : ', popular_day)


    # TO DO: display the most common start hour
    popular_hour = df['hour'].value_counts().idxmax()
    print('Most Frequent Start Hour : ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_used_start = df['Start Station'].value_counts().idxmax()
    print("the Most commonly used start station : ", most_commonly_used_start)

    # display most commonly used end station
    most_commonly_used_end = df['End Station'].value_counts().idxmax()
    print("the Most commonly used end station : ",most_commonly_used_end)

    # display most frequent combination of start station and end station trip
    frequent_stations = df.groupby(['Start Station'])['End Station'].value_counts().idxmax()
    print('the most frequent combination of start station and end station trip : ', frequent_stations)
  
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("total travel time : ",total_travel_time)

    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("mean travel time : ", mean_travel_time)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    print('the counts of user types is : ')
    print(df['User Type'].value_counts())
    print()

    # TO DO: Display counts of gender
    if "Gender" in df:
        print('the counts of gender is : ')
        print(df['Gender'].value_counts())
        print()


    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest=df["Birth Year"].min()
        most_recent=df["Birth Year"].max()
        most_common=df["Birth Year"].value_counts().idxmax()
        print("earliest year of birth : ",earliest)
        print("most recent year of birth : ",most_recent)
        print("most common year of birth : ",most_common)
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def show_data(df):
    """Displays rows ."""
    print('\nDisplays rows...\n')
    count_row =df.shape[0]
    start=0
    end=5
    while(end<count_row):
        user_choice=input('do you need to display the first 5 ? Enter yes or no : ')
        user_choice=user_choice.lower()
        if user_choice=="yes":
            print(df[start:end])
            start=start+5
            end=end+5
            break
        elif user_choice=="no":
            break
        else:
            print("wrong input")


    user_choice=""
    while(end<count_row):
        user_choice=input('do you need to display the next 5 row ? Enter yes or no : ')
        user_choice=user_choice.lower()
        if user_choice=="yes":
            print(df[start:end])
            start=start+5
            end=end+5
        elif user_choice=="no":
            break
        else:
            print("wrong input")
    print('-'*40)
   




    

    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
