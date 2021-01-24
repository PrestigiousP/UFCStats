import json


class Fighter:
    def __init__(self):
        self.id = None
        self.fname = None
        self.lname = None
        self.height = None
        self.weight = None
        self.reach = None
        self.stance = None
        self.dob = None
        self.slpm = None
        self.stracc = None
        self.sapm = None
        self.strdef = None
        self.td = None
        self.tdacc = None
        self.tddef = None
        self.subavg = None
        # # fetch data from json file and create fighters object
        # f = open('fighters.json', 'r')
        # # put json into a dictionary
        # data = json.load(f)
        # # Iterating through the data list
        # for i in data['Name']:
        #     print(i)

        # self.height = None
        # self.weight = None
        # self.reach = None
        # self.stance = None
        # self.dob = None
        # self.slpm = None

