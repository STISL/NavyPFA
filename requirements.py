import sqlite3

def finder(gender, ageGroup, event, goal):
    #create a SQL connection to database:
    connection = sqlite3.connect('NavyPFA_DB.db')
    #create the sqlite3 cursor to use execute methods:
    cursor = connection.cursor()
    #create SQL query as a string statement to pass:
    query = (f"""SELECT {event} FROM PFA_STANDARDS WHERE Gender="{gender}" AND Age_Group="{ageGroup}" AND Performance="{goal}";""")
    #exceute the query:
    cursor.execute(query)
    requirement = cursor.fetchone()
    print(requirement)
    return requirement
    #Close the connection
    connection.close()


#Python SQL query string formatting example:
#Code Sample:

#sql = ("SELECT field1, field2, field3, field4 "
       #"FROM table "
       #"WHERE condition1=1 "
       #"AND condition2=2;")
#Works as well with f-strings:

#fields = "field1, field2, field3, field4"
#table = "table"
#conditions = "condition1=1 AND condition2=2"

#sql = (f"SELECT {fields} "
       #f"FROM {table} "
       #f"WHERE {conditions};")

#Cleanest way I have come across is inspired by the sql style guide.

#sql = """
    #SELECT field1, field2, field3, field4
      #FROM table
     #WHERE condition1 = 1
       #AND condition2 = 2;
#"""







#EXAMPLE BELOW:
#import sqlite3

    # Create a SQL connection to our SQLite database
#con = sqlite3.connect("data/portal_mammals.sqlite")

#cur = con.cursor()

    # Return all results of query
#cur.execute('SELECT plot_id FROM plots WHERE plot_type="Control"')
#cur.fetchall()

    # Return first result of query
#cur.execute('SELECT species FROM species WHERE taxa="Bird"')
#cur.fetchone()

    # Be sure to close the connection
#con.close()
#END EXAMPLE


#import sqlite3

# Create a SQL connection to our SQLite database
#con = sqlite3.connect("data/portal_mammals.sqlite")

#cur = con.cursor()

# The result of a "cursor.execute" can be iterated over by row
#for row in cur.execute('SELECT * FROM species;'):
    #print(row)

# Be sure to close the connection
#con.close()