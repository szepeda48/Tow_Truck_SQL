
import sqlite3
import csv
# from xlwt import Workbook 

# ADDRESS,CAMERA ID,VIOLATION DATE,VIOLATIONS,X COORDINATE,Y COORDINATE,LATITUDE,LONGITUDE,LOCATION
# 7738 S WESTERN,CHI065,07/08/2014,65,,,,,

def create_db_and_table():
    conn = sqlite3.connect("towed-cars.db")
    cursor = conn.cursor()
    sql = "CREATE TABLE tow_table (month int, day int, year int, make text, style text, model text , color text, plate text, state text, street_num int , street_dir text, street_name text )"
    cursor.execute(sql)
    cursor.close()


def add_tow_data_to_database():
    conn = sqlite3.connect("towed-cars.db") 
    cursor = conn.cursor()

    with open("towed_vehicles_city_of_chicago.csv", "r") as f:
        for line in f:
            if not line.startswith("Tow Date"):
                L = line.split(",")
                date = L[0].split("/")
                month = int(date[0])
                day = int(date[1])
                year = int(date[2])
                make = L[1]
                style = L[2]
                model = L[3]
                color = L[4]
                plate = L[5]
                state = L[6]
                towed_address = L[7].split(" ")
                street_num = towed_address[0]
                street_dir = towed_address[1]
                street_name = towed_address[2]

                

                sql = "INSERT INTO tow_table(month, day , year , make , style , model, color, plate, state, street_num, street_dir, street_name) VALUES (:month, :day, :year, :make, :style , :model, :color, :plate, :state, :street_num, :street_dir, :street_name)"
                cursor.execute(sql, {"month": month, "day":day, "year": year, "make":make, "style": style, "model":model, "color": color, "plate":plate, "state": state, "street_num":street_num, "street_dir":street_dir, "street_name":street_name})



                conn.commit()
    cursor.close()


def display_all_db_data():
    conn = sqlite3.connect('towed-cars.db')
    cursor = conn.cursor()

    sql = "SELECT * FROM tow_table" 


    address_column = cursor.execute(sql)

    all_addresses = address_column.fetchall()
    for address in all_addresses:
        print(address)


# # Displayes the whole table 

#    # columns = cursor.execute(sql)
#    # all_entries = columns.fetchall()
#    # for entry in all_entries:
#     #    print(entry)


# def display_out_of_state():
#     conn = sqlite3.connect('towed-cars.db')
#     cursor = conn.cursor()




#     #How many of the cars came from out of state?



#     sql = "SELECT COUNT(state) FROM tow_table WHERE state != 'IL' AND state != '' "

#     #answer :        -------
# #                     (406,)
# #                     -------



#     address_column = cursor.execute(sql)

#     all_addresses = address_column.fetchall()
#     for address in all_addresses:
#         print(address)


# def display_states_in_order():
#     conn = sqlite3.connect('towed-cars.db')
#     cursor = conn.cursor()

#     #Aside from Illinois, list all other states that the towed cars came from, in alphabetical order.


#     sql = "SELECT state FROM tow_table WHERE NOT state = 'IL' ORDER BY state "


#     #Answer:    (u'AL',)  (u'CT',)  (u'IN',)    (u'MN',)   (u'NJ',)   (u'PA',)   (u'WI',)
#     #           (u'AR',)  (u'DE',)  (u'KY',)    (u'MO',)   (u'NM',)   (u'SC',)
#     #           (u'AZ',)  (u'FL',)  (u'LA',)    (u'MS',)   (u'NV',)   (u'TN',)
#     #           (u'B1',)  (u'GA',)  (u'MA',)    (u'MT',)   (u'NY',)   (u'TX',)
#     #           (u'CA',)  (u'IA',)  (u'ME',)    (u'NC',)   (u'OH',)   (u'VA',)
#     #           (u'CO',)  (u'ID',)  (u'MI',)    (u'ND',)   (u'OK',)   (u'WA',)




    
#     address_column = cursor.execute(sql)
#     all_addresses = address_column.fetchall()
#     for address in all_addresses:
#         print(address)


# def display_towing_in_chicago():
#     conn = sqlite3.connect('towed-cars.db')
#     cursor = conn.cursor()

#     #How many towing facility locations are there in the City of Chicago, according to this dataset? NUmber of difference adresses in IL
   
#     sql = "SELECT COUNT (DISTINCT address) FROM (SELECT street_num, street_dir, street_name AS address FROM tow_table WHERE state = 'IL' )"


# #   Answer:  ((4,), ' Different Towing places in Chicago')





    
#     address_column = cursor.execute(sql)
#     all_addresses = address_column.fetchall()
#     for address in all_addresses:
#         print(address, " Different Towing places in Chicago")




# def display_most_towed_day():
#     conn = sqlite3.connect('towed-cars.db')
#     cursor = conn.cursor()

#     #On what date were the most cars towed? What day of the week was this? (Look up the day in a calendar)

#     sql = " SELECT MAX(number_of_rows), month,day, year FROM (SELECT month,day,year,COUNT(*)  AS number_of_rows FROM tow_table GROUP BY  month,day,year)"


#     # Answer: ((132, 4, 12, 2019), 'Friday')




#     address_column = cursor.execute(sql)
#     all_addresses = address_column.fetchall()
#     for address in all_addresses:
#         print(address, "Friday")




# def display_most_towed_manufacturer():
#     conn = sqlite3.connect('towed-cars.db')
#     cursor = conn.cursor()


#     #What vehicle make (i.e. car manufacturer) is the most towed?    



#     sql = " SELECT MAX(number_of_tows), make FROM (SELECT make,COUNT(*)  AS number_of_tows FROM tow_table GROUP BY  make)"



#      #  Answer:   (796, u'CHEV')




#     columns = cursor.execute(sql)
#     all_entries = columns.fetchall()
#     for entry in all_entries:
#         print(entry)




# def work_test():
#     conn = sqlite3.connect('towed-cars.db')
#     cursor = conn.cursor()


#     #What vehicle make (i.e. car manufacturer) is the most towed?    



#     sql = " SELECT month , make FROM tow_table "



#      #  Answer:   (796, u'CHEV')




#     columns = cursor.execute(sql)
#     all_entries = columns.fetchall()
#     for entry in all_entries:
#         print(entry)










def main():
    create_db_and_table()
    add_tow_data_to_database()

    display_all_db_data()
    print("-------")

    # display_out_of_state()
    # print("-------")

    # display_states_in_order()
    # print("-------")

    # display_towing_in_chicago()
    # print("-------")

    # display_most_towed_day()
    # print("-------")
    
    # display_most_towed_manufacturer()
    # print("-------")

    # work_test()
    # print("-------")



main()






