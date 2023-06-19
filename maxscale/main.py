Author: Calvin Davis
Email: cddavis01@student.rtc.edu
Date: 06/17/2023
Class: CNE 370
Description: This script connects to a MaxScale instance, performs various queries on the zipcodes_one and the second database,
and prints the results to the console.
"""

import mysql.connector

# Connect to MaxScale
con = mysql.connector.connect(
    host="10.0.0.99",
    user="maxuser",
    password="maxpwd",
    port="4000"
)
cursor = con.cursor()

# The largest zipcode in zipcodes_one
print("Query: Find the largest zipcode in zipcodes_one")
cursor.execute("SELECT MAX(zipcode) FROM zipcodes_one.zipcodes_one;")
largest_zipcode = cursor.fetchone()[0]
print("Largest Zipcode in zipcodes_one:", largest_zipcode)

# All zipcodes where state=KY (Kentucky) in zipcodes_one
print("Query: Find all zipcodes in Kentucky (zipcodes_one)")
cursor.execute("SELECT zipcode FROM zipcodes_one.zipcodes_one WHERE state = 'KY';")
ky_zipcodes = cursor.fetchall()
print("Zipcodes in Kentucky (zipcodes_one):")
for zipcode in ky_zipcodes:
    print(zipcode[0])

# All zipcodes between 40000 and 41000 in zipcodes_one
print("Query: Find all zipcodes between 40000 and 41000 (zipcodes_one)")
cursor.execute("SELECT zipcode FROM zipcodes_one.zipcodes_one WHERE zipcode BETWEEN 40000 AND 41000;")
zipcodes_range = cursor.fetchall()
print("Zipcodes between 40000 and 41000 (zipcodes_one):")
for zipcode in zipcodes_range:
    print(zipcode[0])

# The TotalWages column where state=PA (Pennsylvania) in zipcodes_one
print("Query: Find the Total Wages in Pennsylvania (zipcodes_one)")
cursor.execute("SELECT TotalWages FROM zipcodes_one.zipcodes_one WHERE state = 'PA';")
total_wages = cursor.fetchall()
print("Total Wages in Pennsylvania (zipcodes_one):")
for wages in total_wages:
    print(wages[0])


# All zipcodes where state=KY (Kentucky) in zipcodes_two
print("Query: Find all zipcodes in Kentucky (zipcodes_two)")
cursor.execute("SELECT zipcode FROM zipcodes_two.zipcodes_two WHERE state = 'KY';")
ky_zipcodes = cursor.fetchall()
print("Zipcodes in Kentucky (zipcodes_two):")
for zipcode in ky_zipcodes:
    print(zipcode[0])

# All zipcodes between 40000 and 41000 in zipcodes_two
print("Query: Find all zipcodes between 40000 and 41000 (zipcodes_two)")
cursor.execute("SELECT zipcode FROM zipcodes_two.zipcodes_two WHERE zipcode BETWEEN 40000 AND 41000;")
zipcodes_range = cursor.fetchall()
print("Zipcodes between 40000 and 41000 (zipcodes_two):")
for zipcode in zipcodes_range:
    print(zipcode[0])

# The TotalWages column where state=PA (Pennsylvania) in zipcodes_two
print("Query: Find the Total Wages in Pennsylvania (zipcodes_two)")
cursor.execute("SELECT TotalWages FROM zipcodes_two.zipcodes_two WHERE state = 'PA';")
total_wages = cursor.fetchall()
print("Total Wages in Pennsylvania (zipcodes_two):")
for wages in total_wages:
    print(wages[0])

# Close the database connection
con.close()
