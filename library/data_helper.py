import csv
import mysql.connector

def read_csv_data(filepath):
    data =[]
    # with open("C:/Users/User/OneDrive/Desktop/Selenium_LMS/Constants/data/saucedemo_login.csv") as csvfile:
    with open(filepath)  as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
            # print(row)
        # print(data[0])
    return data

def read_mysql_data(fetch_query):
    # Establish the connection
    cnx =  mysql.connector.connect(user='root' , password='maayi@283', 
                                host='localhost', database='tgsql')
    
    # Create cursor object
    cursor = cnx.cursor()
    query = fetch_query
    cursor.execute(query)
    
    #  Fetch the data
    data =  cursor.fetchone()
    print(data)
    if data:
        user_name = data[0]
        password = data [1]
        print("USERNAME:", user_name)
        print("PASSWORD:", password)
    else:
        print("NO USER FOUND")
        
    # Close Connection
    cursor.close()
    cnx.close()
    return data