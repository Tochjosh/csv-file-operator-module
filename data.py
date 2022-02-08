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

