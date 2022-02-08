import csv
import time

from data import Data


class InputOutputData:
    raw_array = []  # this array stores the dataset from the csv
    length = 0

    def read_data(self):
        """
        this method reads the csv file
        """
        self.raw_array = []
        file_path = input("Enter the correct file path to load file ")
        print('''               searching for file...''')
        time.sleep(2)

        try:
            """
            opening up csv file using the file path variable declared and assigning it to the file variable
            """
            file = open(file_path, 'r')
            # reader = csv.reader(file)
            # lines = len(list(reader))

            row_number = 0
            for each_line in file:
                """
                we read each line split it by comma and then placed it in a memory array
                """
                split_line = each_line.split(",")

                if row_number == 0:
                    self.length = len(split_line)  # set the number of column names as the length of row
                    row_number += 1
                    continue

                if row_number >= 1:
                    if len(split_line) > self.length:
                        split_line.pop()

                    data = Data(row_number, *split_line)
                    self.raw_array.append(data)
                    row_number += 1

            file.close()
            return True
        except IOError:
            print(file_path + ' file not found in path')
            return False

    def show_records_in_array(self):
        """
        Show all records from array
        """
        for i in self.raw_array:
            print(i)
        time.sleep(2)

    def create_new_record(self, new_data):
        """
        Create a new record and store it in the simple data structure
        """
        self.raw_array.append(new_data)
        print("New record was added successfully!")

    def edit_record_by_id(self, id, new_data):
        """
        Edit records of specific data using its ID
        """
        self.raw_array[id] = new_data
        print(new_data)
        print("Record has been edited successfully!")

    def delete_record_by_id(self, id):
        """
        Delete any record from Array by ID using the del function
        """
        del self.raw_array[id]
        print("Record has been deleted successfully!")

    def display_all_records(self):
        """
        View all records in dataset
        """
        for i in self.raw_array:
            print(i)

        print("All record printed successfully")

    def check_record(self, id):
        """
        check if a record exists using the id
        """
        for i in self.raw_array:
            if i.id == id:
                return True
        return False

    def search_by_multiple_columns(self, col_list, val_list):
        """
        search record based on multiple column at the same time
        """

        result = []
        try:
            for data in self.raw_array:
                truity = []
                for i in col_list:
                    if type(getattr(data, i)) is int:
                        if getattr(data, i) == int(val_list[col_list.index(i)]):
                            truity.append(True)
                        else:
                            truity.append(False)
                    else:
                        if getattr(data, i).lower() == str(val_list[col_list.index(i)]).lower():
                            truity.append(True)
                        else:
                            truity.append(False)

                    if all(truity):
                        result.append(data)

        except AttributeError:
            print('Details not found. Please try again correctly')
            time.sleep(2)
            return False

        print('''   filtering...  ''')
        time.sleep(2)
        if len(result) == 0:
            print("No match(es) found!")
            time.sleep(2)
        else:

            print('''                     ---- Match(es) ----''')

        for i in result:
            print(i)
        return result
