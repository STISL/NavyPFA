#Program displays Navy PFA passing requirements for specific PRT events based on user input.

#import sqlite3 to use as a database:
import sqlite3
#finder function will execute SQL queries
#from requirements import finder
from DB_creator import createDatabase

#create the database to use for program:
createDatabase()
#Greeting for user:
print(f"\n* * * * * * * * * * *\nHello, this program will tell you what you need to score in a Navy PFA event in order to earn points and a desired performance category for that event.\n* * * * * * * * * * *\n")

#User must input 'm' or 'f' to indicate gender through while loop and try/if/except statement:
while True:
    try:
        gender = str(input(f"\n* * * * * * * * * * *\nWhat is your gender?\nType 'm' for male or 'f' for female: ")).lower()
        if (gender == 'm') or (gender == 'f'):
            break
        print(f"\nInvalid gender entered. Try again.")
    except Exception as e:
        print(e)

#User must input valid age as an integer through while loop and try/if/except statement:
while True:
    try:
        age = int(input(f"\n* * * * * * * * * * *\nWhat is your current age as a whole number? "))
        if (age >= 17):
            break
        print(f"\nInvalid age entered. Minimum age requirement is 17. \nTry again.")
    except Exception as e:
        print(e)

#Create dictionary for PFA events with nomenclature to match SQLite tables:
dict_PFA_events = {1:"Push-Ups",2:"Forearm Planks",3:"1.5-mile Run",4:"2-km Row",5:"450-meter Swim",6:"500-yard Swim",7:"Stationary Bike",8:"Treadmill"}
  
#User selects key for PFA event through while loop and try/if/except statement:
while True:
    try:
        eventSelected = int(input(f"""\n* * * * * * * * * * *\nEnter number for PFA event you are doing:
\n[1]: Push-Ups
[2]: Forearm Planks
[3]: 1.5-mile Run
[4]: 2-km Row
[5]: 450-meter Swim
[6]: 500-yard Swim
[7]: Stationary Bike
[8]: Treadmill
\n"""))
        if (eventSelected >= 1) or (eventSelected <= 7):
            event = dict_PFA_events[eventSelected]
            break
        print(f"n\Invalid selection entered. Try again.")
    except Exception as e:
        print(e)

#Step5 - Create dictionaries for specific event's performance categories and required score for that category:
#WILL BE A MODULE TO IMPORT!

#Create dictionary for PFA performance categories:
dict_PFA_perfCats ={1:"Probationary",2:"Satisfactory Medium",3:"Satisfactory High",4:"Good Low",
5:"Good Medium",6:"Good High", 7:"Excellent Low",8:"Excellent Medium",9:"Excellent High",10:"Outstanding Low",11:"Outstanding Medium",12:"Outstanding High"}

#Create dictionary for PFA performance points:
dict_perfPoints = {"Probationary":"45","Satisfactory Medium":"50","Satisfactory High":"55","Good Low":"60","Good Medium":"65","Good High":"70","Excellent Low":"75","Excellent Medium":"80","Excellent High":"85","Outstanding Low":"90","Outstanding Medium":"95","Outstanding High":"100"}

#User selects category they want to score in through while loop and try/if/except statement:
while True:
    try:
        perfSelected = int(input(f"""\n* * * * * * * * * * *\nEnter number for performance category you want to get for your event.
\n[1]: Probationary (minimum required to pass, but means mandatory enrollment in FEP)
[2]: Satisfactory Medium
[3]: Satisfactory High
[4]: Good Low
[5]: Good Medium
[6]: Good High
[7]: Excellent Low (minimum required to become a CFL)
[8]: Excellent Medium
[9]: Excellent High
[10]: Outstanding Low
[11]: Outstanding Medium 
[12]: Outstanding High
\n"""))
        if (perfSelected >= 1) and (perfSelected <= 12):
            goal = dict_PFA_perfCats[perfSelected]
            points = dict_perfPoints[goal]
            break
        print(f"n\Invalid selection entered. Try again.")
    except Exception as e:
        print(e)

#Conditions based on gender and Navy PFA age categories = 17-19, 20-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59, 60-64, 65+:
if (gender == 'm'):
    gender = 'male'
    if (age >= 17) and (age <= 19):
        ageGroup = '17 to 19'
    elif (age >= 20) and (age <= 24):
        ageGroup = '20 to 24'
    elif (age >= 25) and (age <= 29):
        ageGroup = '25 to 29'
    elif (age >= 30) and (age <= 34):
        ageGroup = '30 to 34'
    elif (age >= 35) and (age <= 39):
        ageGroup = '35 to 39'
    elif (age >= 40) and (age <= 44):
        ageGroup = '40 to 44'
    elif (age >= 45) and (age <= 49):
        ageGroup = '45 to 49'
    elif (age >= 50) and (age <= 54):
        ageGroup = '50 to 54'
    elif (age >= 55) and (age <= 59):
        ageGroup = '55 to 59'
    elif (age >= 60) and (age <= 64):
        ageGroup = '60 to 64'
    elif (age >= 65):
        ageGroup = '65 or older'
else: 
    if (gender == 'f'):
        gender = 'female'
        if (age >= 17) and (age <= 19):
            ageGroup = '17 to 19'
        elif (age >= 20) and (age <= 24):
            ageGroup = '20 to 24'
        elif (age >= 25) and (age <= 29):
            ageGroup = '25 to 29'
        elif (age >= 30) and (age <= 34):
            ageGroup = '39 to 34'
        elif (age >= 35) and (age <= 39):
            ageGroup = '35 to 39'
        elif (age >= 40) and (age <= 44):
            ageGroup = '40 to 44'
        elif (age >= 45) and (age <= 49):
            ageGroup = '45 to 49'
        elif (age >= 50) and (age <= 54):
            ageGroup = '50 to 54'
        elif (age >= 55) and (age <= 59):
            ageGroup = '55 to 59'
        elif (age >= 60) and (age <= 64):
            ageGroup = '60 to 64'
        elif (age >= 65):
            ageGroup = '65 or older'

#finder function will access the NavyPFA_DB file created and return a result for the requirement variable:
def finder(gender, ageGroup, event, goal):
    #reassign event names to matching required headers in the database table:
    if (event == 'Push-Ups'):
        event = 'Push_Ups'
    elif (event == 'Forearm Planks'):
        event = 'Forearm_Planks'
    elif (event == '1.5-mile Run'):
        event = 'One_and_Half_Mile_Run'
    elif (event == '2-km Row'):
        event = 'Two_Kilometer_Row'
    elif (event == '450-meter Swim'):
        event = 'FourHundredFifty_Meter_Swim'
    elif (event == '500-yard Swim'):
        event = 'FiveHundred_Yard_Swim'
    elif (event == 'Stationary Bike'):
        event = 'Stationary_Bike'
    else:
        event = event
    #create a SQL connection to database:
    connection = sqlite3.connect('NavyPFA_DB.db')
    #create the sqlite3 cursor to use execute methods:
    cursor = connection.cursor()
    #execute a SQLite query to get requirement from database:
    cursor.execute(f"""SELECT {event} FROM PFA_STANDARDS WHERE Gender="{gender}" AND Age_Group="{ageGroup}" AND Performance="{goal}";""")
    #use the str.join() method on cursor.fetchone to reformat the tuple fetched:
    result = ''.join(cursor.fetchone())
    return result

#pass inputted argument values into imported finder function
#finder function gets & returns score needed:
requirement = finder(gender, ageGroup, event, goal)
#display results:
print(f"\n* * * * * * * * * * *\nYou are a {age}-year old {gender} in the {ageGroup} year-old age group.")
print(f"You have chosen to do the {event}.")
print(f"In order to receive a mark of {goal} for {points} points")
print(f"you will need to {requirement}.")
print("\nGOOD LUCK!\n")

