
class Person:

    #def set_first_name(self, firstName): #self: this method belongs to this class
        #self.first_name = firstName #make up a property of the class "firstName"
    
    def __init__(self, firstName, middleName, lastName):
        if not isinstance(firstName, str):
            print('Bad boy!')

        self.first_name = firstName
        self.middle_name = middleName
        self.last_name = lastName #creates three properties

    def __str__(self):
        return self.first_name + ' ' + \
        self.middle_name[0] + '. ' + self.last_name #self is the parameter