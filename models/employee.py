import json

from models.model import *

class employee():

    """
    A class that models an employee
    ...

    Methods
    -------
    load_employee(file_name)
        Loads employee json file
    
    toJSON(self)
        Serializes json file
    """

    def __init__(self):
        self.globalData = {"message":"Hello from Flask!", "ok":"true"}
        self.filename = ".\data\employees.json"
        self.employee = self.load_employee(self.filename)

    # Load employee json file
    def load_employee(self, filename):
        my_model = model()
        instance = my_model.load_db(filename)
        
        return instance

    # Returns one employee from employee json based on employee ID
    def __getitem__(self, i):
        return self.employee[i]

    # Serializes json file
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4, separators=(',', ': '))

    # Getter property decorator for employee
    @property
    def employee(self):
        return self._employee

    # Setter property decorator for employee
    @employee.setter
    def employee(self, value):
        self._employee = value