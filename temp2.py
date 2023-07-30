import time
import os
import csv
from csv import reader
import pandas as pd
import matplotlib.pyplot as plt
##Future Imports go above here

def LoadFile():
    timetable = os.path.abspath("Timetable2022.csv")  # gets the file path of the csv file
    with open(timetable, "r") as f:
        pass
    content = open(timetable)  # opens and reads the files
    readcontent = csv.reader(content)
    rows = []  # stores all the rows in a large multi array, starting with the headings, and then each array being each individual date with the times of each train. Format: [[Headings], [Date, Train 1 time, Train 2 time, Train 3 time, Train 4 time, Train 5 time], [Date, .......... ]]
    for row in readcontent:
        rows.append(row)
    return (rows)

    # readcontent[0] - heading, readcontent[1][0] - date, readcontent[1][1] - first train on said date
    # total number of dates = 366


def ArrivalTimes():
    timetable = LoadFile()  # sends in the row array from the previous function and stores it in variable
    checker = 0  # the checker is set to 0, so that it will allow the following while loop to be preformed
    while checker == 0:  # while loop is designed so that the user can only input the options avaliable. If they do not, the question is promted again until they pick a suitable answer.
        print('You are now able to:\n1 - View The Entire Timetable\n2 - An Individual Train')
        checker2 = 0
        while checker2 == 0:
            choice = input('Which option will you pick: ')
            if choice == '1':
                for i in range(1, 366):  # creates a for loop which goes 366 times (number of days in array)
                    print('Date: ', timetable[i][0])  # prints out the date
                    for j in range(1, 6):  # creates another loop which consists of the trains
                        print("Train ", j, ":", timetable[i][j])  # then prints out the trains
                checker2 = checker2 + 1
                print('returning to menu...')
                time.sleep(2)
                menu()
            elif choice == '2':
                checker1 = 0
                while checker1 == 0:
                    train = int(input(
                        "please input the train you would like to search up times for: "))  # asks the user for which train number they are looking for
                    if train > 5 or train < 1:
                        print(" SORRY, THAT TRAIN DOES NOT EXIST ON OUR TIMETABLE, PLEASE CHOOSE A DIFFERENT TRAIN")
                    else:
                        for i in range(1, 366):
                            print('Date: ', timetable[i][0])  # prints out the date
                            print("Train", train, ":", timetable[i][train])  # prints out the corresponding train
                    checker1 = 1  # stops loops
                checker2 = 1
                print('returning to menu...')
                time.sleep(2)
                menu()
            else:
                print("YOU HAVE ENTERED AN INCORRECT VALUE, PLEASE TRY AGAIN ")


def ManageTimes():  # Function which allows the user to search for a specific train or look
    timetable = LoadFile()  # loading file
    checker = 0  # loop to prevent errors and allows users to retype
    onlyMonth = False
    while checker == 0:
        choice = input(
            'would you like to:\n1 - Search for a specific train by date and time\n2 - Update arrival time\nPlease select and option:  ')  # \n - new line : choice one -> user will be allowed to look for a specific train by inputting the date and the time of the train  choice 2 -> User is able to make changes to the times store in the csv file
        if choice == '1':
            checker = 1
            print("Alright, i will now be asking you the day and month you would specifically like to look at ")
            monthcollection = TrainLocatorM(timetable, True, False)  # collects the month which the user has requested
            checker4 = 0
            while checker4 == 0:
                choice2 = input(
                    'would you like to know all the train times in said month, or just look for a single day (option 1 or option 2): ')  # gives the user the option to look through the months or skip to finding the specific train using the date
                if choice2 == '1':
                    for i in range(0,
                                   len(monthcollection)):  # checks the length of the array, then prints out the date, followed by the trains of said date, then moves to the next date, until the entire month is printed
                        print('Date: ', monthcollection[i][0])
                        for j in range(1, 6):
                            print("Train ", j, ":", monthcollection[i][j])
                    checker4 = 1
                    print('returning to menu...')
                    time.sleep(2)
                    menu()
                elif choice2 == '2':
                    trainSpecific = TrainLocatorD(timetable, monthcollection, 0)
                    print('Here are the trains for the time period: ', trainSpecific[0])  # prints out the time period
                    for m in range(1, 6):  # aswell as the trains in said time period
                        print("Train", m, ":", trainSpecific[m])
                    print('returning to menu...')
                    time.sleep(2)
                    menu()
                    checker4 = 1
                else:
                    print(
                        "YOU HAVE ENTERED AN INCORRECT VALUE, PLEASE TRY AGAIN ")  # prompts the user to retype due to inputting an invalid option
        elif choice == '2':
            checker = 1
            dateToEdit, position = TrainLocatorM(timetable, False,
                                                 False)  # collects the exact train the user is looking for, and position said train is in the array. This is useful as it will locate the line the day appears on the csv file
            checker5 = 0
            while checker5 == 0:  # loop to prevent mistakes
                for i in range(1, 6):  # prints out all the trains in said date for the user to choose from
                    print('Train', i, ':', dateToEdit[i])
                trainUser = int(input('please select the train with the incorrect time: '))
                if trainUser > 5 or trainUser < 1:
                    print(
                        " SORRY, THAT TRAIN DOES NOT EXIST ON OUR TIMETABLE, PLEASE CHOOSE A DIFFERENT DATE")  # error prompted when user inputs something not in the range
                else:
                    trainHours = dateToEdit[trainUser][0] + dateToEdit[trainUser][
                        1]  # takes the hours in the train the user has picked
                    trainMinutes = dateToEdit[trainUser][3] + dateToEdit[trainUser][
                        4]  # takes the minutes in the train the user has picked
                    checker6 = 0
                    trainUser = str(
                        trainUser)  # converts the users input into a string so that it can be used in the following print line
                    while checker6 == 0:
                        choice3 = input(
                            'Train ' + trainUser + ' is in operation at ' + trainHours + ':' + trainMinutes + ' today.\n Would you like to change this Train? (y/n) : ')  # confirmation that they picked the correct time
                        if choice3 == 'n':  # if they didnt, go back and retype
                            checker6 = 1
                        elif choice3 == 'y':  # if they did, then proceed
                            checker6 = 1
                            checker7 = 0
                            while checker7 == 0:
                                newHour = int(input(
                                    'please select the new hour(24 hour format): '))  # asks the user to type in the new hour
                                if newHour > 23 or newHour < 0:
                                    print(
                                        'YOU HAVE INPUTTED AN INVALID TIME PERIOD, PLEASE SELECT AGAIN')  # prompt is its out of the range
                                else:
                                    newMinute = int(input(
                                        'please enter the new minutes: '))  # asks user to type  in the new minutes
                                    if newMinute > 59 or newMinute < 0:
                                        print(
                                            'YOU HAVE INPUTTED AN INVALID TIME PERIOD, PLEASE SELECT AGAIN')  # prompt is its out of the range
                                    else:
                                        checker7 = 1
                                        newHour = str(
                                            newHour)  # convers the hour the user inputted, and checks the length so that if they only inputted 1 digit, an 0 is added in front (for the spreadsheet formatting)
                                        if len(newHour) == 1:
                                            newHour = newHour.zfill(2)
                                        newMinute = str(newMinute)
                                        print('Ok, changing the time from', trainHours + ':' + trainMinutes, 'to',
                                              newHour + ':' + newMinute)
                                        doc = pd.read_csv("Timetable2022.csv")  # opens the csv file
                                        position = position - 2  # the position of the date in relation to the array and the position said date is in the spreadsheet is off by 2, so we deduct to allow program to match the right date in the spreadsheet
                                        trainHeading = 'Train ' + trainUser  # looks for the heading with the words 'Train' and the number associated by the user
                                        doc.loc[
                                            position, trainHeading] = newHour + ':' + newMinute  # replaces the item in the specific cell with what the user inputted
                                        doc.to_csv('Timetable2022.csv', index=False)
                                        print('returning to menu.. ')  # returns to menu
                                        time.sleep(2)
                                        menu()
        else:  # if neither, then print and error and redo
            print("YOU HAVE ENTERED AN INCORRECT VALUE, PLEASE TRY AGAIN ")


def TrainLocatorM(timetable, onlyMonth, monthNeeded):
    checker3 = 0
    while checker3 == 0:
        month = int(input(
            "what is the month you would like to look at (1 - 12): "))  # Asks the user to input a value between 1 and 12 corresponding to the month
        if month > 12 or month < 1:
            print(
                " SORRY, THAT TRAIN DOES NOT EXIST ON OUR TIMETABLE, PLEASE CHOOSE A DIFFERENT MONTH")  # month range, will promt the user to retype
        else:
            checker3 = 1
            month = str(
                month)  # converts the int 'month' to a string, this allows us to add a zero if the userinput only enters a single digit. If it were a single digit, it wont match the data in the excel file, which has no single digits on the dates. (i.e 9th of march is written as 09/03 not 9/3 on the excel file)
            if len(month) == 1:
                month = month.zfill(2)  # adds a zero infront of the digit if the string is only 1 character
            monthcollection = []  # stores the months
            for k in range(1,
                           366):  # this loop checks the dates to see if they are the same as the date inputted by the user. If the first number of the month the user inputted = the first number of the excel file month, it will check the second. If that also matches, it will add it to the month list and move onto the next date
                if month[0] == timetable[k][0][3]:
                    if month[1] == timetable[k][0][4]:
                        monthcollection.append(timetable[k])
                        if len(monthcollection) == 1:
                            monthPosition = k
                k = k + 1
            if onlyMonth == True and monthNeeded == False:  # function is used for many things, and different things need to be returned for different functions. This allows the right information to be returned to the right array, given the right boolean responses
                return (monthcollection)
            elif monthNeeded == True and monthNeeded == True:
                return month, monthcollection
            else:
                return TrainLocatorD(timetable, monthcollection, monthPosition)


def TrainLocatorD(timetable, monthcollection, monthPosition):
    choice4 = 0
    while choice4 == 0:
        length = str(len(monthcollection))
        day = int(input(
            'please enter in the correct date for the train you would like to look for (1 - ' + length + '): '))  # promts the user to input the date they are looking for
        if day > len(monthcollection) or day < 1:
            print(
                " SORRY, THAT TRAIN DOES NOT EXIST ON OUR TIMETABLE, PLEASE CHOOSE A DIFFERENT DATE")  # if number is out of range, print and prompt them to retype
        else:
            choice4 = 1
            day = str(
                day)  # same as months, changed int into string to allow the addition of a zero of the string has a length of 1
            if len(day) == 1:
                day = day.zfill(2)
            trainSpecific = ''
            for l in range(0,
                           len(monthcollection)):  # again, checks the dates against the dates in the arrays, and if they are the same in both regards, they are added to the variable 'trainSpecific']
                if day[0] == monthcollection[l][0][0] and day[1] == monthcollection[l][0][1]:
                    trainSpecific = monthcollection[l]
                intday = int(day)
                datePosition = monthPosition + intday
                if monthPosition > 0 and len(trainSpecific) == 6:
                    return trainSpecific, datePosition
                elif len(trainSpecific) == 6:
                    return trainSpecific


def AnalysisGraph():
    timetable = LoadFile()  # imports file
    date = []  # stores the dates
    trainTimes = []  # stores the train times in seconds
    trains = []  # stores the train times in actual time
    y = []  # stores the intervals for the y axis
    x = []  # stores the intervals for the x axis
    dateCollection = []  # collects the 1st day of each month
    f, ax = plt.subplots()
    checker = 0  # to prevent misinputs
    while checker == 0:
        train = int(input("What train would you like to see the arrival times for: "))
        if train > 5 or train < 0:
            print('YOU HAVE INPUTTED AN INCORRECT VALUE, PLEASE RETRY')
        else:
            checker = 1
    for i in range(1, len(timetable)):
        if timetable[i][0][0] == '0' and timetable[i][0][1] == '1':
            x.append(i)  # appends the 1st day of the month to the x array
            dateCollection.append(timetable[i][0])  # appends the actual date (used as the label)
        date.append(timetable[i][0])  # adds all the dates to the array
        trains.append(timetable[i][
                          train])  # adds the train time (which the user specified for) for the entire year into spreadsheet
        hour = int(timetable[i][train][0] + timetable[i][train][
            1])  # the time in the spreadsheet is converted into seconds and stored in their respected y arrays
        mins = int(timetable[i][train][3] + timetable[i][train][4])
        seconds = 3600 * hour + 60 * mins
        trainTimes.append(seconds)
    maxi, mini = MiniMax(train, trains)  # finds the minimum and maximum times in the month
    multiples_between = []  # stores the multiples between the minimum and maximum
    setTicks = []  # array used to set ticks
    difference = maxi - mini  # finds the range
    decider = (
                          difference // 900) + 1  # divides range by 900 seconds (15 mins)  -> the intervals of the graph is supposed to be every 15 mins, but whilst testing, the dates seemed to be joined up and difficult to read
    if decider > 62:  # and so, a limit is used to allow the y axis divisions to still be visable. If beyond a certain amount, the intervals will be every 30mins (1800 seconds), else, continue with every 15 mins
        multiplier = 1800
    else:
        multiplier = 900
    intervals = difference // 62
    wholeMin = (
                mini // multiplier)  # divides the lowest amount of seconds by the divisions, the process behind this is to get the lowest division and highest divisions by finding what multiple is closest to the lowest and highest time found in the month
    mini = multiplier * wholeMin  # this is the minimum time rounded down to the nearest 15 mins
    wholeMax = (maxi // multiplier) + 1
    maxi = multiplier * wholeMax  # this is the maximum time round up to the nearest 15 mins
    for i in range(wholeMin,
                   wholeMax + 1):  # within the range of the amount of divisions between the highest and the lowest times, it will convert each multiple of 900 or 1800 between the highest and lowest number from seconds to hours and minutes, and then will store to be used as tick labels
        summed = multiplier * i
        newHrs = (summed) // 3600
        newMins = ((summed) % 3600) // 60
        Hrs = str(newHrs)
        Mins = str(newMins)
        if len(Mins) == 1:
            Mins = Mins.zfill(2)
        multiples_between.append(Hrs + ':' + Mins)
        y.append(
            multiplier * i)  # y will be used as the actual ticks, so we would need to know the actual divisions in seconds
    train = str(train)
    ax.plot(date, trainTimes, color='b', linestyle='-', label='Train ')  # plots the arrays onto the graphs, and assigns them properties
    plt.xticks(rotation=25)
    plt.xlabel('Dates')  # x and y labels
    plt.ylabel('Time')
    plt.title('Arrival Times for Train'+train, fontsize=30)
    plt.legend()
    ax.set_xticks(x)  # sets the intervals to be first of every month
    ax.set_yticks(
        y)  # sets the intervals on the y axis to be the amount of intervals between the highest and lowest time in seconds
    ax.set_yticklabels(multiples_between)  # labels the y axis intervals in the hr:min format
    ax.set_xticklabels(
        dateCollection)  # labels the dates to the correct dates (before adding this, the dates were set to the 02 of each month rather than the first)
    plt.show()  # prints grid
    print('returning to menu...')
    time.sleep(2)
    menu()


def MiniMax(train, traintime):  # finds the minimum and maximum train time in a selected month in seconds
    minimum = 0
    maximum = 0
    for i in range(0, len(traintime)):  # this for loop looks at each indivdual hour and minute
        hour = int(traintime[i][0] + traintime[i][1])
        minute = int(traintime[i][3] + traintime[i][4])
        seconds = hour * 3600 + minute * 60
        if i == 0:  # if the value is zero for minimum, assume the first time is the lowest (to prevent minimum staying on zero)
            minimum = seconds
        if seconds > maximum:  # if the seconds is higher than the maximum value, then replace it
            maximum = seconds
        elif seconds < minimum:  # if not, then check if it is lower than the minimum value
            minimum = seconds
    return maximum, minimum


def Schedule():
    checker = 0  # allows a loop to be generated so that the user is prompted to input the correct value
    while checker == 0:
        print(
            "Would you like to:\n1 - Run schedule for the departure of a certain train\n2 - Run Schedule for all trains")  # gives user the choice of what is outputted on the live timetable and for how long
        choice = input('Please choose and option: ')
        if choice == '1':
            checker1 = 0  # again, another loop maker to allow users to reattempt
            while checker1 == 0:
                train = int(input(
                    "please input the train you would like to be updated on: "))  # prompts the user to input the train they would like to use
                if train > 5 or train < 0:
                    print(
                        "THIS TRAIN IS NOT REGISTERED ON THE SYSTEM, PLEASE INPUT THE CORRECT TRAIN")  # prompts user to reinput due to an incorrect value
                else:
                    trainSchedule(False, train,
                                  0)  # sends of the train the user would like to be updated on into the next function (designed to output the live broadcast of when the train is coming), sends to the program that there are not multiple trains, the specific train they would like to know about is what they inputted, and that they want the program to run infinitely (default = 0)
                    checker1 = 1
        elif choice == '2':
            checker2 = 0  # loop maker to allow users to reattempt
            while checker2 == 0:
                tHours = int(input(
                    'please input the amount of hours you would like the run the program for: '))  # prompts the user to input how long they would like to run the program
                if tHours < 0:
                    print(
                        'YOU HAVE INPUTTED AN INVALID TIME PERIOD, PLEASE SELECT AGAIN')  # prompts user to reinput due to an incorrect value
                tMinutes = int(input('please input the amount of minutes you would like to run the program for: '))
                if tMinutes > 59 or tMinutes < 0:
                    print(
                        'YOU HAVE INPUTTED AN INVALID TIME PERIOD, PLEASE SELECT AGAIN')  # prompts user to reinput due to an incorrect value
                tSeconds = (tHours * 3600) + (tMinutes * 60)  # converts the time into seconds
                trainSchedule(True, 0,
                              tSeconds)  # sends the amount of seconds the user wants the program running for. Tells function that there are multiple trains, there is no specific train they want(default = 0) and that they want the program to run for tSeconds


        else:
            print(
                '!!!!YOU HAVE INPUTTED AN INVALID RESPONSE, PLEASE TRY AGAIN!!!!')  # prompts user to reinput due to an incorrect value


def trainSchedule(multiTrain, Train, tSeconds):
    timetable = LoadFile()  # loading file
    choice = ''  # creates and infinite loop, designed so that the user can
    start = time.time()  # gets the epoch time(in seconds), used later to compare how long the program has been running for
    while choice != 'x':
        timeToday = time.ctime(time.time())  # collects the current epoch time (not the start time)
        print(timeToday)  # prints todays date
        if timeToday[4] == 'D':  # checks todays date, and assigns is numerical equivalent
            month = 12
        elif timeToday[4] == 'F':
            month = 2
        elif timeToday[4] == 'N':
            month = 11
        elif timeToday[4] == 'O':
            month = 10
        elif timeToday[4] == 's':
            month = 9
        elif timeToday[4] == 'A':
            if timeToday[5] == 'p':
                month = 4
            else:
                month = 8
        elif timeToday[4] == 'M':
            if timeToday[6] == 'r':
                month = 3
            else:
                month = 5
        elif timeToday[4] == 'J':
            if timeToday[5] == 'a':
                month = 1
            elif timeToday[5] == 'u':
                if timeToday[6] == 'n':
                    month = 6
                else:
                    month = 7
        month = str(month)  # converts the int to a string to allow a zero in front of the number (felt more convient)
        if len(month) == 1:
            month = month.zfill(
                2)  # checks the date and the month of today, and compares it to whats found on the spreadsheet. When said date is found, add it to a variable
        for i in range(1, 366):
            day = timeToday[8] + timeToday[9]
            if timeToday[8] == ' ':
                day = '0' + timeToday[9]
            if day[0] == timetable[i][0][0]:
                if day[1] == timetable[i][0][1]:
                    if month[0] == timetable[i][0][3]:
                        if month[1] == timetable[i][0][4]:
                            currentDay = timetable[i]
        hour = timeToday[11] + timeToday[12]  # locates todays time in hours seconds and minutes
        minute = timeToday[14] + timeToday[15]
        second = timeToday[17] + timeToday[18]
        hour = int(hour)  # turns them into an int
        minute = int(minute)
        second = int(second)
        totalSeconds = hour * 3600 + minute * 60 + second  # converts the time today into seconds
        for i in range(1, 6):  # creates a for loop to repeat 6 times
            if multiTrain == False:
                i = Train  # if there is only one train, set the train the user wants to i
            hourTable = currentDay[i][0] + currentDay[i][1]
            minTable = currentDay[i][3] + currentDay[i][4]
            hourTable = int(hourTable)  # convers them into ints
            minTable = int(minTable)
            totalSecondsTable = hourTable * 3600 + minTable * 60  # calculates the total time in seconds
            difference = totalSecondsTable - totalSeconds  # finds the difference between the amount of seconds until the train arrives, and the amount of seconds that have passed today
            newHrs = difference // 3600  # converts the results back into hours and minutes
            newMins = (difference % 3600) // 60
            departed = False  # sets a boolean
            if newHrs < 0:  # if the results of the difference puts the hours in minus, then the trains must have departed already
                print('Train', i, 'has already departed')
                departed = True  # sets boolean to true
            elif newHrs == 0:  # if the newhrs is zero
                if (newMins <= 20 and newMins % 5 == 0) or (
                        newMins < 5):  # and the remaining minutes are 20, 15, 10, 5, 4, 3, 2 and 1, the user is alerted that the train is near and should be ready to board
                    print("!!!!!!! TRAIN", i, "WILL BE DEPARTING IN", newMins,
                          "MINUTES, PLEASE BE READY TO BOARD!!!!!!")
                elif newMins == 0:  # and there are no minutes, the train is arriving and the user should be boarding
                    print('!!!!!!!!!! TRAIN IS HAS ARRIVED AND IS NOW DEPARTING !!!!!!!!!!!')
                else:  # there are some minutes left until the train arrives
                    print('Train', i, 'is approaching in : ', newMins, ' mins')
            else:  # if the train time still has hours, print out how many hours and minutes remain
                print('Train', i, 'is approaching in : ', newHrs, 'hrs and ', newMins, 'mins')
            if multiTrain == False:  # implimented so that this only runs once, it will print out the time for the train the user wants and not print it again 4 more times
                break
        timePassed = time.time() - start  # after the loop is completed, it will check how long the program has been running since the start
        if tSeconds > 58:  # program takes 0.3 is seconds to run, so if it were tSeconds > 60, and the user wanted the program to run for a minute, this section wouldnt run as the difference in time would be less than 60, so 58 was used
            timeTaken = tSeconds - timePassed  # checks the difference between how long the user wanted the program to run for and how long is left
            if timeTaken <= 600 and timeTaken > 540:  # if the program has 10 mins left before it closes, this message is printed
                print('!!!!!THE PROGRAM WILL CLOSE IN LESS THAN 10 MINUTES!!!!')
            elif timeTaken <= 300 and timeTaken > 240:  # if the program has 5 mins left before it closes, this message is printed
                print('!!!!!THE PROGRAM WILL CLOSE IN LESS THAN 5 MINUTES!!!!')
            elif timeTaken <= 60 and timeTaken > 1:  # if the program has 1 mins left before it closes, this message is printed
                print('!!!!!THE PROGRAM WILL CLOSE IN LESS THAN 60 SECONDS!!!!')
            elif timeTaken <= 0:  # once the time is completed, the user is taken back to the main menu
                print('!!!!!TIME CONCLUDED, NOW TAKING YOU TO THE MAIN MENU!!!!')
                time.sleep(2)
                choice = 'x'  # closes the while loop
                menu()
        elif departed == True and multiTrain == False:  # if the train has departed, and there is only one train being reviewed, the program stops and you are taken to the main menu
            print('This train has departed, returning you to the main menu...')
            time.sleep(2)
            menu()
        time.sleep(60)
        os.system('cls')  # cmd clears the terminal


def menu():
    # Starting menu options, basic interface
    print("-----------------TimeTable-----------------")
    print(
        "Good day, here are your avaliable options: \n1 - Arrival Times(Time Table for all or specific trains in the year) \n2 - Manage Timetable(look for the time of a specific train on a specific date / update your timetable) \n3 - Anaylse Timetable (produce an arrival time graph) \n4 - Set Schedules(A live updating train schedule for your day today)\nx - Quit ")
    checker = 0
    while checker == 0:
        choice = input("please input the option you would like to go with: ")  # users option
        if choice == '1':
            print('working 1')
            ArrivalTimes()  # runs arrival time function
            checker = checker + 1  # checker = checker + 1 - breaks the while loop and ensures that the question wont be asked again
        elif choice == '2':
            ManageTimes()  # runs managing time function
            checker = checker + 1
        elif choice == '3':
            AnalysisGraph()  # runs analysis function
        elif choice == '4':
            Schedule()  # runs schedule function
            checker = checker + 1
        elif choice == 'x':
            checker2 = 0  # again like checker 1, to prevent miss inputs
            while checker2 == 0:
                choice2 = input(
                    "are you sure you would like to quit the program (yes or no) ")  # say the user doesnt want to quit, there is a secondary confirmation for it
                if choice2 == 'yes':  # last confirmation
                    exit(1)
                elif choice2 == 'no':
                    print('Ok, asking again...')
                    checker2 = 1
                    time.sleep(1)  # time.sleep(1) - pauses the program for 1 second
                else:
                    print(
                        " YOU HAVE INPUTTED AN INVALID OPTION, ANSWER AGAIN")  # program telling the user that what they inputted is not on the list and to retry it
                    time.sleep(1)
        else:
            print(
                " YOU HAVE INPUTTED AN INVALID OPTION, ANSWER AGAIN")  # program telling the user that what they inputted is not on the list and to retry it
            time.sleep(1)


menu()
