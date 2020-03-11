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
    cities = ['chicago', 'new york city', 'washington']
    city = ""
    print("Please enter a city from the following list: ", cities)
    while not city in cities:
        city = input().lower()
        if not city in cities:
            print("City not recognized, please try again")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'juni']
    month = ""
    print("Please enter a month from the following list: ", months)
    while not month in months:
        month = input().lower()
        if not month in months:
            print("Month not recognized, please try again")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ""
    print("Please day of the week from the following list: ", days)
    while not day in days:
        day = input().lower()
        if not day in days:
            print("Day not recognized, please try again")


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
    
    print("We have successfully read the data file you requested. Would you like to see a sample (yes/no)?")
    spl = ""
    while spl not in ['yes', 'no']:
        spl = input().lower()
        if spl not in ['yes', 'no']:
            print("Just say 'yes' or 'no' OK?")
    if spl == 'yes':
        print(df.head(5))
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    df['Trip'] = df['Start Station'] + ' - ' + df['End Station']

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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    """Useful comment number 1"""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common stuff
    print("Most common month: ", df['month'].mode()[0])
    print("Most common day of the week: ", df['day_of_week'].mode()[0])
    print("Most common hour: ", df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display the most common stuff
    # TO DO: display most commonly used start station
    print("Most common start station: ", df['Start Station'].mode()[0])
    # TO DO: display most commonly used end station    
    print("Most common end station: ", df['End Station'].mode()[0])
    
    # TO DO: display most frequent combination of start station and end station trip    
    
    print("Most common start-end combo: ", df['Trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display mean travel time
    print("Average trip duration: {:.1f}".format( df['Trip Duration'].mean() ))

    # TO DO: display total travel time
    print("Total trip duration: {:.0f}".format( df['Trip Duration'].sum() ))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types: ")
    cts = df['User Type'].value_counts().iteritems()
    for val, cnt in cts:
        print("   Type ",val," has count ",cnt)
    print("")

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print("Counts of genders: ")
        cts = df['Gender'].value_counts().iteritems()
        for val, cnt in cts:
            print("   Type ",val," has count ",cnt)
    else:
        print("No gender info available for this city")
    print("")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("Earliest year of birth: {:.0f}".format(df['Birth Year'].min()))
        print("Most recent year of birth: {:.0f} ".format(df['Birth Year'].max()))
        print("Most common year of birth: {:.0f}".format(df['Birth Year'].mode()[0]))
    else:
        print("No birth year info available for this city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()