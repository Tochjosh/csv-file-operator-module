import unittest
from data import Raw
from controller import IORaw


class TestProject(unittest.TestCase):

    def test_read_over(self):
        """
        test how the program reads in records if its placing data into correct fields of record object
        read file
        """
        io_raw = IORaw()
        io_raw.read_data()
        new_id = len(io_raw.raw_array) + 1
        raw_data = Raw(new_id, 32, 'Josuha', 'Lekan', '2021-11-16', 'Agro-BioTech', 4839, 32763
                       , 0, 0.40, 0.2810, 0.00, 3764, 9272, 2999373, 2523)

        """Test column"""
        self.assertEqual(raw_data.pruid, 32)
        self.assertEqual(raw_data.prename, 'Josuha')
        self.assertEqual(raw_data.prfname, 'Lekan')
        self.assertEqual(raw_data.week_end, '2021-11-16')
        self.assertEqual(raw_data.product_name, 'Agro-BioTech')
        self.assertEqual(raw_data.numtotal_atleast1dose, 4839)
        self.assertEqual(raw_data.numtotal_partially, 32763)
        self.assertEqual(raw_data.numtotal_fully, 0)
        self.assertEqual(raw_data.prop_atleast1dose, 0.40)
        self.assertEqual(raw_data.prop_partially, 0.2810)
        self.assertEqual(raw_data.prop_fully, 0.00)
        self.assertEqual(raw_data.numweekdelta_atleast1dose, 3764)
        self.assertEqual(raw_data.numweekdelta_fully, 9272)
        self.assertEqual(raw_data.propweekdelta_partially, 2999373)
        self.assertEqual(raw_data.propweekdelta_fully, 2523)

    def test_create_new_record(self):
        """
        Check if new record is appended correctly to underlying data structure

        reading through file
        """
        io_raw = IORaw()
        io_raw.read_data()
        last_inserted_id = len(io_raw.raw_array)
        new_id = last_inserted_id + 1

        raw_sample = Raw(new_id, 21, 'william', 'joshua', '2021-11-16', 'Agro_biotech', 2460, 12240
                         , 0, 0.60, 0.810, 0.20, 134, 2233, 222343, 12232)

        """
        adding data
        """
        io_raw.create_new_record(raw_sample)

        """
        asserts true if record added exists
        """
        self.assertTrue(io_raw.check_record(new_id))

    def test_edit_record_by_id(self):
        """
        check if an existing record is updated as expected
        read through file
        """

        io_raw = IORaw()
        io_raw.read_data()
        last_inserted_id = len(io_raw.raw_array)
        new_id = last_inserted_id + 1

        raw_data = Raw(new_id, 47, 'Bobokoso', 'mzeebabu', '2020-01-02', 'Pfizer-ss', 3540, 35440
                       , 0, 0.30, 0.310, 0.00, 121, 2323, 233423, 12132)
        """
        Create New Record
        """
        io_raw.create_new_record(raw_data)

        """
        Update Record
        """
        raw_data2 = Raw(new_id, 47, 'Jonnasburgg', 'lefidahia', '2021-11-16', 'Agro', 3540, 35440
                        , 0, 0.30, 0.310, 0.00, 121, 2323, 233423, 12132)

        record_to_edit = new_id - 1
        io_raw.edit_record_by_id(record_to_edit, raw_data2)

        """
        Assert True if record is successfully updated
        """
        updated_vaccine = io_raw.raw_array[record_to_edit]
        self.assertEqual(updated_vaccine.prename, 'Jonnasburgg')
        self.assertEqual(updated_vaccine.prfname, 'lefidahia')
        self.assertEqual(updated_vaccine.week_end, '2021-11-16')
        self.assertEqual(updated_vaccine.product_name, 'Agro')

        self.assertTrue(io_raw.check_record(new_id))

    def test_delete_record_by_id(self):
        """
        Pytest to check records are deleted
        read file
        """

        io_raw = IORaw()
        io_raw.read_data()
        last_inserted_id = len(io_raw.raw_array)
        new_id = last_inserted_id + 1

        raw_data = Raw(new_id, 47, 'deletemeVaccine', 'mzeebabu', '2020-01-02', 'Pfizer-ss', 3540, 35440
                       , 0, 0.30, 0.310, 0.00, 121, 2323, 233423, 12132)
        """
        ADD DATA
        """
        io_raw.create_new_record(raw_data)

        """
        Delete Record by Id
        """
        record_to_delete = new_id - 1
        io_raw.delete_record_by_id(record_to_delete)

        """
        Assert True if record by id not found(404)
        """
        self.assertFalse(io_raw.check_record(new_id))

    def test_record_not_existing(self):
        """
        Pytest to check if record isn't found, search query == Id

        Read Through File
        """

        io_raw = IORaw()
        io_raw.read_data()
        last_inserted_id = len(io_raw.raw_array)

        """
        Create a non esisting ID
        """
        non_existing = last_inserted_id + 10
        raise_error = False

        try:
            io_raw.check_record(non_existing)
        except IndexError:
            raise_error = True

        self.assertFalse(raise_error, "Record Does Not Exist!!")


if __name__ == '__main__':
    unittest.main()
