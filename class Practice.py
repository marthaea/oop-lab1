class Student:
    def__init__(self, name, gpa):
        self.namet = name #public
        self._age = 20 #protected 
        self.__gpa = 4.5#private
        
    def get_gpa(self):
        return self.__gpa
        
    def set_gpa(self, value):
        if 0.0 <= 5.0:
            self.gpa = value 
        else:
            print('GPA must be between 0 and 5')
   #Next set up objects
    