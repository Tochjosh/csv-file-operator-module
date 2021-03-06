from controller import InputOutputData
from data import Data
import time


def menu():
    print('''
                            --- Starting Process ---
                                 --- MENU ---
    1. Reload the data from the dataset, replacing the data structure or database.
    2. Display all the records held in the simple data structure.
    3. Create a new record and store it in the simple data structure or database.
    4. Select and edit a record held in the simple data structure in memory by id.
    5. Select and delete a record from the simple data structure in memory by id.
    6. Search multiple columns at the same time.
    7. Exit.
    ''')


def multiple_search():
    col_list = []
    val_list = []

    def column(lis):
        col_name = input('Enter correct column name (case sensitive):\n')
        lis.append(col_name)
        response = input("Do you wish to enter another column name [y/n]\n").lower()
        if response == 'y':
            column(lis)
        elif response == 'n':
            return lis
        else:
            column(lis)

    def value(lis):
        val = input('Enter the values in the correct order:\n')
        lis.append(val)
        while len(lis) < len(col_list):
            res = input("Enter the next value\n").lower()
            lis.append(res)
        return lis

    print("Enter the columns you'll like to search by one at a time")
    column(col_list)
    print('Enter the values to search by respectively')
    value(val_list)

    return [col_list, val_list]


def user_inputs():
    """
    To insert new record or to edit an old record we prompt user for each value
    and puts it in the array structure memory
    """
    pruid = input("Enter pruid: ")
    prename = input("Enter prename: ")
    prfname = input("Enter prfname: ")
    week_end = input("Enter week_end: ")
    product_name = input("Enter product_name: ")
    numtotal_atleast1dose = input("Enter numtotal_atleast1dose: ")
    numtotal_partially = input("Enter numtotal_partially: ")
    numtotal_fully = input("Enter numtotal_fully: ")
    prop_atleast1dose = input("Enter prop_atleast1dose: ")
    prop_partially = input("Enter prop_partially: ")
    prop_fully = input("Enter prop_fully: ")
    numweekdelta_atleast1dose = input("Enter numweekdelta_atleast1dose: ")
    numweekdelta_fully = input("Enter numweekdelta_fully: ")
    propweekdelta_partially = input("Enter propweekdelta_partially: ")
    propweekdelta_fully = input("Enter propweekdelta_fully: ")

    data = Data(len(io_raw.raw_array) + 1, pruid, prename, prfname, week_end, product_name,
                numtotal_atleast1dose,
                numtotal_partially, numtotal_fully, prop_atleast1dose, prop_partially,
                prop_fully, numweekdelta_atleast1dose, numweekdelta_fully, propweekdelta_partially,
                propweekdelta_fully)
    return data


print('''               --- WELCOME ---   ''')
io_raw = InputOutputData()
"""
if read file is successful and file is record_found successful
"""
if io_raw.read_data():
    io_raw.show_records_in_array()
    time.sleep(2)
    menu()

    choice = input("Enter your choice: ")
    while choice != "7":
        if choice != "7":
            print('''                --- processing... --- ''')

        if choice == "1":
            io_raw.show_records_in_array()
        elif choice == "2":
            print("........ Loading all Records ....... \n")
            io_raw.show_records_in_array()
        elif choice == "3":
            io_raw.create_new_record(user_inputs())
        elif choice == "4":
            id = input("To edit record enter id: ")
            record_record_found = io_raw.check_record(int(id))
            if record_record_found:
                new_id = int(id) - 1
                io_raw.edit_record_by_id(new_id, user_inputs())
            else:
                print("Record does not exist")
        elif choice == "5":
            id = input("Enter id: ")
            record_found = io_raw.check_record(int(id))
            if record_found:
                new_id = int(id) - 1
                io_raw.delete_record_by_id(new_id)
            else:
                print("Record does not exist")
        elif choice == "6":
            args = multiple_search()
            if args:
                io_raw.search_by_multiple_columns(*args)
            else:
                time.sleep(2)
                menu()
        else:
            print("Invalid choice")

        menu()
        """
        we loop until user enters 7 then exits from the application
        """
        choice = input("Please enter your choice: ")
