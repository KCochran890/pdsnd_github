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
    city = ''
    while city not in CITY_DATA.keys():
        print("Hello, please input the name of your city: Washington, New York, or Chicago.")
        city = input().lower()
    print ('You have chosen ' + city.title() + '.')
    # TO DO: get user input for month (all, january, february, ... , june)
    MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all']
    month = ''
    while month not in MONTHS:
        print("Please input the month you would like to review.")
        month = input().lower()
    print('Hello! You have chosen: ' + month.title() + '.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_OF_WEEK = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in DAY_OF_WEEK:
        print('Please input the day of the week you would like to review: ')
        day = input().lower()
    print('You have chosen: ' + day.title()+ '.')          
   
    
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

    
    most_common_month = df['month'].mode()[0]
    print('Most popular month: {most_common_month}.')
    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]
    print('Most popular day: {most_common_day}.')
    # TO DO: display the most common start hour
    df['hour'] = ['Start Time'].dt.hour
    popular_start_time = df['hour'].mode()[0]
    print('Most popular start time: {popular_start_time}.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_starting_location = df['Start Station'].mode()[0]

    print("The most commonly used start station: " + common_starting_location)

    # TO DO: display most commonly used end station
    common_ending_location = df['End Station'].mode()[0]

    print("The most commonly used end station: " + common_ending_location)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combination = df['Start To End'].mode()[0]

    print("The most frequent combination of trips are from " + combination + ".")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_trip_time = df['Trip Duration'].sum() 
    mins, second = divmod(total_trip_time, 60)
    hrs, mins = divmod(mins, 60)
    print("The total trip time is: {hrs} hours and {mins} minutes.")

    # TO DO: display mean travel time
    avg_travel_time = round(df['Trip Duration'].mean())
    mins, sec = divmod(avg_travel_time, 60)
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print("The average trip duration is {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe average trip duration is {mins} minutes and {sec} seconds.")
            

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("The count of users by gender is: " + gender)
    except:
        print("There is no gender data.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print("The earliest year of birth is: " + earliest + ". The most recent year of birth is: " + most_recent + ". The most common year of birth is: " + most_common_year)
    except:
        print("There is no gender data.")
           

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        #time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
