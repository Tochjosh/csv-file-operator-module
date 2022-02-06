from data import Raw
import os.path
from pathlib import Path


class InputOutputRaw:
    raw_array = []  # this array stores the dataset from the csv

    def read_data(self):
        """
        this method reads the csv file
        """
        self.raw_array = []
        file_path = "../vaccination-coverage-byVaccineType.csv"
        split_by = ","
        counter = 0

        try:
            """
            opening up csv file using the file path variable declared and assigning it to the file variable
            """
            file = open(file_path, 'r')
            for i in file:
                """
                we read each line split it by comma and then placed it in a memory array
                """
                each_line = i
                split_line = each_line.split(split_by)

                if counter >= 1:
                    data = Raw(counter, split_line[0], split_line[1], split_line[2], split_line[3], split_line[4],
                               split_line[5], split_line[6], split_line[7], split_line[8],
                               split_line[9], split_line[10], split_line[11], split_line[12], split_line[13],
                               split_line[14])
                    self.raw_array.append(data)
                    counter += 1

                if counter == 0:
                    counter += 1
                if counter >= 120:
                    break
            file.close()
            return 1
        except IOError:
            print(file_path + ' file not found in path')
            return 0

    def show_records_in_array(self):
        """
        Show all records from array
        """
        for i in self.raw_array:
            print(i)

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
        Read specific record from array using its ID
        """

        for i in self.raw_array:
            return i

        print("All record has been sucessfully printed")

    def check_record(self, id):
        """
        check for record using that id.exists()
        """
        count = 0
        for i in self.raw_array:
            if i.id == id:
                count += 1
                break

        if count == 0:
            return 0
        else:
            return 1

    def search_by_multiple_columns(self, col_list, val_list):

        """
        search record based on multiple column at the same time
        """

        result = []
        for data in self.raw_array:
            truity = []
            for i in col_list:
                if type(getattr(data, i)) is int:
                    if getattr(data, i) == int(val_list[col_list.index(i)]):
                        truity.append(1)
                    else:
                        truity.append(0)
                else:
                    if getattr(data, i).lower() == str(val_list[col_list.index(i)]).lower():
                        truity.append(1)
                    else:
                        truity.append(0)

            if all(truity):
                result.append(data)

        print('Matche(s)')
        print('---------------')
        for i in result:
            print(i)

        return result