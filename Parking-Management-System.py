#Parking Management System
#Name : Muhammad Noor-ul-Hassan
#Roll No : F21BSEEN1E02009
import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle")



import cx_Oracle
conn=cx_Oracle.connect('noor/12345678@//localhost:1521/xe')
print("Orcale, is connected to ",conn.version, " version of database.")

cur=conn.cursor()

#GET CLIENT & VEHICLE DETAILS

def details_function():
    print("************************CUSTOMER DETAILS************************")
    ID   = input('Enter customer ID                      : ')
    name   = input('Enter customer name                    : ')
    email  = input('Enter customer email                   : ')
    phone1 = input('Enter customer phone number            : ')
    phone2 = input('Enter customer emergency phone number  : ')
    print("************************ VEHICLE DETAILS ************************")
    vehicle_nbr   = input('Enter vehicle plate number             : ')
    print("\nOnly CAR , BIKE & CYCLE are applicable ******")
    vehicle_type  = input('Enter vehicle type                     : ')
    vehicle_model = input('Enter vehicle model                    : ')
    vehicle_color = input('Enter vehicle color                    : ')
    if vehicle_type == 'bike':
        fee = int(100)
    elif vehicle_type == 'car':
        fee = int(500)
    elif vehicle_type == 'cycle':
        fee = int(50)
    else:
        print('************************ Entered wrong vehicle type ************************\n'
              '************************ Please refill details ************************')
        details_function()
    print("************************LOCATION DETAILS************************")
    block    = input('Enter block number                    : ')
    row      = input('Enter row number                      : ')
    position = input('Enter position                        : ')

# Save data to database
    query1 = "insert into customer_table values('{}','{}','{}','{}','{}')".format(ID, name, email, phone1, phone2)
    cur.execute(query1)

    query2 = "insert into vehicle_table values('{}','{}','{}','{}','{}','{}')".format(ID,vehicle_model,vehicle_type,vehicle_color,vehicle_nbr,fee)
    cur.execute(query2)

    query3 = "insert into location_table values('{}','{}','{}','{}')".format(ID, block,row, position)
    cur.execute(query3)

    conn.commit()
    print("************************ Data saved to database ************************")
    input()
    print('\npress 1 to go back')
    print('press 2 to go main menu')
    print('press 3 to exit')
    choice2 = int(input("\nENTER YOUR CHOICE : "))
    if choice2 == 1:
        details_function()
    elif choice2 == 2:
        main()
    elif choice2 == 3:
        exit()
    else:
        print('************************ Entered invalid key ************************')
        input()
        main()

#search data from database

def search_function():
    print("************************** DETAILS CENTRE **********************************")
    print("*     1.search customer details                                            *")
    print("*     2.search vehicle  details                                            *")
    print('*     3.search vehicle location                                            *')
    print("****************************************************************************")
    choice1 = int(input("ENTER YOUR CHOICE : "))
    if choice1 == 1:
        ID = input("Enter your ID : ")
        query = "select * from customer_table where customer_id='{}'".format(ID)
        cur.execute(query)
        data = cur.fetchone()

        if data is None:
            print('\33[31mNo Data found with ID:\33[0m', ID)
            print('---------------------------')
        else:
            print('*************************** CUSTOMER DETAILS ***********************')
            print('|', "ID               : ", data[0], '|')
            print('|', "NAME             : ", data[1], '|')
            print('|', "EMAIL            : ", data[2], '|')
            print('|', "PHONE NUMBER     : ", data[3], '|')
            print('|', "EMERGENCY NUMBER : ", data[4], '|')
            print('********************************************************')
            print('press 1 to go back')
            print('press 2 to go main menu')
            print('press 3 to exit')
            choice2 = int(input("\nENTER YOUR CHOICE : "))
            if choice2 == 1:
                search_function()
            elif choice2 == 2:
                main()
            elif choice2 == 3:
                exit()
            else:
                print('************************ Entered invalid key ************************')
                input()
                main()

    elif choice1 == 2:
        vehicle_nbr = input("Enter Your  vehicle number : ")
        query = "select * from vehicle_table where vehi_number='{}'".format(vehicle_nbr)
        cur.execute(query)
        data = cur.fetchone()

        if data is None:
            print('\33[31mNo Data found with Vehicle Number:\33[0m', vehicle_nbr)
            print('---------------------------')
        else:
            print('*************************** Vehicle Details ***********************')
            print('|', "vehicle model       : ", data[1], '|')
            print('|', "vehicle type        : ", data[2], '|')
            print('|', "vehicle color       : ", data[3], '|')
            print('|', "vehicle number      : ", data[4], '|')
            print('|', "vehicle parking fee : ", data[5], '|')
            print("************************************************************************")
            print('press 1 to go back')
            print('press 2 to go main menu')
            print('press 3 to exit')
            choice2 = int(input("\nENTER YOUR CHOICE : "))
            if choice2 == 1:
                search_function()
            elif choice2 == 2:
                main()
            elif choice2 == 3:
                exit()
            else:
                print('************************ Entered invalid key ************************')
                input()
                main()

    elif choice1 == 3:
        ID = input("Enter Your ID : ")
        query = "select * from location_table where location_id='{}'".format(ID)
        cur.execute(query)
        data = cur.fetchone()

        if data is None:
            print('\33[31mNo Data found with ID:\33[0m', ID)
            print('---------------------------')
        else:
            print('*************************** Vehicle Location Details***********************')

            print('|'"Block number    : ", data[1], '|')
            print('|'"Row number      : ", data[2], '|')
            print('|'"Position in row : ", data[3], '|')
            print()
            print('\npress 1 to go back')
            print('press 2 to go main menu')
            print('press 3 to exit')
            choice2 = int(input("\nENTER YOUR CHOICE : "))
            if choice2 == 1:
                search_function()
            elif choice2 == 2:
                main()
            elif choice2 == 3:
                exit()
            else:
                print('************************ Entered invalid key ************************')
                input()
                main()
    else:
        print("************************ Invalid choice ************************\n"
              "************************ Please Again Enter Your Choice ************************")
        input()
        search_function()

#delete data from database

def delete_function():
    ID = input("Enter your ID                   : ")
    query = "select * from customer_table where customer_id='{}'".format(ID)
    cur.execute(query)
    data = cur.fetchall()

    if data is None:
        print('\33[31mNo Data found with ID:\33[0m', ID)
        print('---------------------------')
    else:
        query1 = "delete from location_table where location_id='{}'".format(ID)
        cur.execute(query1)
        query2 = "delete from vehicle_table where vehi_owner_id='{}'".format(ID)
        cur.execute(query2)
        query3 = "delete from customer_table where customer_id='{}'".format(ID)
        cur.execute(query3)

        conn.commit()
        print('************************************************************************')
        print('RECORD OF USER ID ', ID, 'HAS BEEN DELETED')
        print('************************************************************************')
        print('Press 1 to go back')
        print('Press 2 to go main menu')
        print('Press 3 to exit')
        choice2 = int(input("\nENTER YOUR CHOICE : "))
        if choice2 == 1:
            delete_function()
        elif choice2 == 2:
            main()
        elif choice2 == 3:
            exit()
        else:
            print('************************ Entered invalid key ************************')
            input()
            main()

#update data from database

def update_function():
    ID            =input("Enter customer ID whose data you want to update : ")
    query = "select * from customer_table where customer_id= '{}'".format(ID)
    cur.execute(query)
    data = cur.fetchall()

    if data is None:
        print('\33[31mNo Data found with ID:\33[0m', ID)
        print('---------------------------')
    else:
        print('Enter Updated Data of User ID ', ID)
        name = input("\nEnter updated name                              : ")
        email = input("Enter new email address                         : ")
        phone1 = input("Enter phone number                              : ")
        phone2 = input("Enter emergency phone number                    : ")
        vehicle_nbr = input('Enter vehicle plate number                      : ')
        print('\nOnly CAR,BIKE &CYCLE applicable****************************')
        vehicle_type = input('Enter vehicle type                              : ')
        vehicle_model = input('Enter vehicle model                             : ')
        vehicle_color = input('Enter vehicle color                             : ')
        if vehicle_type == 'bike':
            fee = int(100)
        elif vehicle_type == 'car':
            fee = int(500)
        elif vehicle_type == 'cycle':
            fee = int(50)
        else:
            print('************************ Entered Wrong vehicle type ************************\n'
                  '************************ Please again fill form     ************************')
            input()
            update_function()
        block = input('Enter block number                              : ')
        row = input('Enter row number                                : ')
        position = input('Enter position                                  : ')

        query1 = "update customer_table SET CUSTOMER_NAME='{}',CUSTOMER_EMAIL='{}',PHN_NBR='{}',EMG_PHN_NBR='{}'" \
                 " where CUSTOMER_ID='{}'".format(name, email, phone1, phone2, ID)
        cur.execute(query1)

        query2 = "update vehicle_table SET VEHI_NUMBER='{}',VEHI_COLOR='{}',VEHI_MODEL='{}',VEHI_TYPE='{}'" \
                 " where VEHI_OWNER_ID='{}'".format(vehicle_nbr, vehicle_color, vehicle_model, vehicle_type, ID)
        cur.execute(query2)

        query3 = "update location_table SET BLOCK_NUM='{}',ROW_NUM='{}',POSITION='{}'" \
                 " where LOCATION_ID='{}'".format(block, row, position, ID )
        cur.execute(query3)

        conn.commit()
        print("************************ Data Updated To Database ************************")
        input()
        print('\npress 1 to go back')
        print('press 2 to go main menu')
        print('press 3 to exit')
        choice2 = int(input("\nENTER YOUR CHOICE : "))
        if choice2 == 1:
            update_function()
        elif choice2 == 2:
            main()
        elif choice2 == 3:
            exit()
        else:
            print('************************ Entered invalid key ************************')
            input()
            main()

#Display data from database

def display_function():
    query = "select c.customer_name,c.customer_id,c.customer_email,c.phn_nbr,c.emg_phn_nbr," \
            "v.vehi_number,v.vehi_color,v.vehi_model,v.vehi_type,v.fee,l.block_num,l.row_num,l.position" \
            " from customer_table c join vehicle_table v on(c.customer_id=v.vehi_owner_id) " \
            " join location_table l  on(c.customer_id=l.location_id) "
    cur.execute(query)

    position = 1
    for row in cur:
        print('***************************************')
        print('|','Record no         : ', position)
        print('***************************************')

        print('|', "NAME             : ", row[0], '|')
        print('|', "ID               : ", row[1], '|')
        print('|', "EMAIL            : ", row[2], '|')
        print('|', "PHONE_NO         : ", row[3], '|')
        print('|', "EMERGENCY_NO     : ", row[4], '|')

        print('|', "VEHICLE NO       : ", row[5], '|')
        print('|', "VEHICLE COLOR    : ", row[6], '|')
        print('|', "VEHICLE MODEL    : ", row[7], '|')
        print('|', "VEHICLE TYPE     : ", row[8], '|')
        print('|', "PARKING FEE      : ", row[9], '|')

        print('|', "PARKING BLOCK    : ", row[10], '|')
        print('|', "VEHICLE row      : ", row[11], '|')
        print('|', "PARKING posiion  : ", row[12], '|')
        print('************************************************************************')

        position = position + 1

    print('\npress 1 to go back')
    print('press 2 to go main menu')
    print('press 3 to exit')
    choice2 = int(input("\nENTER YOUR CHOICE : "))
    if choice2 == 1:
        display_function()
    elif choice2 == 2:
        main()
    elif choice2 == 3:
        exit()
    else:
        print('************************ Entered invalid key ************************')
        input()
        main()

#main function
def main():
    choice = 0
    while True:
        print("*********************** Welcome to PARKING SYSTEM ***********************")
        print("*     1.INSERT NEW CUSTOMER DETAILS AND VEHICLE DETAILS                 *")
        print("*     2.search the data                                                 *")
        print('*     3.delete the data                                                 *')
        print('*     4.update the data                                                 *')
        print("*     5.display the data                                                *")
        print("*     6.EXIT                                                            *")
        print("*************************************************************************")
        choice = int(input("ENTER YOUR CHOICE:"))

        if choice == 1:
            details_function()
        elif choice == 2:
            search_function()
        elif choice == 3:
            delete_function()
        elif choice == 4:
            update_function()
        elif choice == 5:
            display_function()
        elif choice == 6:
            exit()
        else:
            print("*********************** Entered wrong choice ***********************\n \n "
                  "*********************** please Try again ***********************")
            input()
            main()


main()