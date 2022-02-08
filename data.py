import datetime


class Data:
    # class attributes
    id = 0
    pruid = 0
    prename = ""
    prfname = ""
    week_end = datetime.datetime.now()
    product_name = ""
    numtotal_atleast1dose = 0
    numtotal_partially = 0
    numtotal_fully = 0
    prop_atleast1dose = 0.0
    prop_partially = 0.0
    prop_fully = 0.0
    numweekdelta_atleast1dose = 0
    numweekdelta_fully = 0
    propweekdelta_partially = 0.0
    propweekdelta_fully = 0.0

    # Initialise all the instance default variables so its accessible by all methods 
    def __init__(self, id, pruid, prename, prfname, week_end, product_name, numtotal_atleast1dose,
                 numtotal_partially, numtotal_fully, prop_atleast1dose, prop_partially,
                 prop_fully, numweekdelta_atleast1dose, numweekdelta_fully, propweekdelta_partially,
                 propweekdelta_fully):
        self.id = id
        self.pruid = pruid
        self.prename = prename
        self.prfname = prfname
        self.week_end = week_end
        self.product_name = product_name
        self.numtotal_atleast1dose = numtotal_atleast1dose
        self.numtotal_partially = numtotal_partially
        self.numtotal_fully = numtotal_fully
        self.prop_atleast1dose = prop_atleast1dose
        self.prop_partially = prop_partially
        self.prop_fully = prop_fully
        self.numweekdelta_atleast1dose = numweekdelta_atleast1dose
        self.numweekdelta_fully = numweekdelta_fully
        self.propweekdelta_partially = propweekdelta_partially
        self.propweekdelta_fully = propweekdelta_fully

    # toString() method of Vaccine class which displays the data of all the properties of Covid
    def __str__(self):
        return f"Data (id = {self.id}, pruid = {self.pruid}, prename = {self.prename}, prfname = {self.prfname}, " \
               f"week_end = {self.week_end}, product_name = {self.product_name}, numtotal_atleast1d" \
               f"ose = {self.numtotal_atleast1dose}, numtotal_partially = {self.numtotal_partially}, numtotal_fully" \
               f"= {self.numtotal_fully}, prop_atleast1dose = {self.prop_atleast1dose}, prop_partially = " \
               f"{self.prop_partially}, prop_fully = {self.prop_fully}, numweekdelta_atleast1dose = " \
               f"{self.numweekdelta_atleast1dose}, numweekdelta_fully = {self.numweekdelta_fully}, " \
               f"propweekdelta_partially = {self.propweekdelta_partially}, propweekdelta_fully = " \
               f"{self.propweekdelta_fully}) "

    # Setting parent methods for all the instance variables

    def set_id(self, id):
        self.id = id

    def set_pruid(self, pruid):
        self.pruid = pruid

    def set_prename(self, prename):
        self.prename = prename

    def set_prfname(self, prfname):
        self.prfname = prfname

    def set_week_end(self, week_end):
        self.week_end = week_end

    def set_product_name(self, product_name):
        self.product_name = product_name

    def set_numtotal_atleast1dose(self, numtotal_atleast1dose):
        self.numtotal_atleast1dose = numtotal_atleast1dose

    def set_numtotal_partially(self, numtotal_partially):
        self.numtotal_partially = numtotal_partially

    def set_numtotal_fully(self, numtotal_fully):
        self.numtotal_fully = numtotal_fully

    def set_prop_atleast1dose(self, prop_atleast1dose):
        self.prop_atleast1dose = prop_atleast1dose

    def set_prop_partially(self, prop_partially):
        self.prop_partially = prop_partially

    def set_prop_fully(self, prop_fully):
        self.prop_fully = prop_fully

    def set_numweekdelta_atleast1dose(self, numweekdelta_atleast1dose):
        self.numweekdelta_atleast1dose = numweekdelta_atleast1dose

    def set_numweekdelta_fully(self, numweekdelta_fully):
        self.numweekdelta_fully = numweekdelta_fully

    def set_propweekdelta_partially(self, propweekdelta_partially):
        self.propweekdelta_partially = propweekdelta_partially

    def set_propweekdelta_fully(self, propweekdelta_fully):
        self.propweekdelta_fully = propweekdelta_fully


# inheriting from parent class Data
class Raw(Data):
    # instance attribute
    id = 1
    pruid = 1
    prename = ""
    prfname = ""
    week_end = datetime.datetime.now()
    product_name = ""
    numtotal_atleast1dose = 0
    numtotal_partially = 0
    numtotal_fully = 0
    prop_atleast1dose = 0.0
    prop_partially = 0.0
    prop_fully = 0.0
    numweekdelta_atleast1dose = 0
    numweekdelta_fully = 0
    propweekdelta_partially = 0.0
    propweekdelta_fully = 0.0

    def __init__(self, id, pruid, prename, prfname, week_end, product_name, numtotal_atleast1dose,
                 numtotal_partially, numtotal_fully, prop_atleast1dose, prop_partially,
                 prop_fully, numweekdelta_atleast1dose, numweekdelta_fully, propweekdelta_partially,
                 propweekdelta_fully):
        """
        THIS inherit the intialization method property of class Data
        """
        super().__init__(id, pruid, prename, prfname, week_end, product_name, numtotal_atleast1dose,
                         numtotal_partially, numtotal_fully, prop_atleast1dose, prop_partially,
                         prop_fully, numweekdelta_atleast1dose, numweekdelta_fully, propweekdelta_partially,
                         propweekdelta_fully)

    # Setting methods for all the instance variables to overide parent class method

    def set_id(self, id):
        self.id = id
        print(self.id)

    def set_pruid(self, pruid):
        self.pruid = pruid

    def set_prename(self, prename):
        self.prename = prename

    def set_prfname(self, prfname):
        self.prfname = prfname

    def set_week_end(self, week_end):
        self.week_end = week_end

    def set_product_name(self, product_name):
        self.product_name = product_name

    def set_numtotal_atleast1dose(self, numtotal_atleast1dose):
        self.numtotal_atleast1dose = numtotal_atleast1dose

    def set_numtotal_partially(self, numtotal_partially):
        self.numtotal_partially = numtotal_partially

    def set_numtotal_fully(self, numtotal_fully):
        self.numtotal_fully = numtotal_fully

    def set_prop_atleast1dose(self, prop_atleast1dose):
        self.prop_atleast1dose = prop_atleast1dose

    def set_prop_partially(self, prop_partially):
        self.prop_partially = prop_partially

    def set_prop_fully(self, prop_fully):
        self.prop_fully = prop_fully

    def set_numweekdelta_atleast1dose(self, numweekdelta_atleast1dose):
        self.numweekdelta_atleast1dose = numweekdelta_atleast1dose

    def set_numweekdelta_fully(self, numweekdelta_fully):
        self.numweekdelta_fully = numweekdelta_fully

    def set_propweekdelta_partially(self, propweekdelta_partially):
        self.propweekdelta_partially = propweekdelta_partially

    def set_propweekdelta_fully(self, propweekdelta_fully):
        self.propweekdelta_fully = propweekdelta_fully
