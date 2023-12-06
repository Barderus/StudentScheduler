class Course:
    '''
        Simple class for representing a course with number, name,
        and credit hours.'
        Created by Carolyn England
        Copyright College of DuPage and Carolyn England
    '''
    
    def __init__(self, num = '', name = '', crHours = 0):
        ''' The __init__ method initializes the
            course object characteristics
            as private data members.
        '''
        self.__num = num
        self.__name = name
        self.__crHours = crHours

    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, n):
        self.__num = n

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, n):
        self.__name = n

    @property
    def crHours(self):
        return self.__crHours
    @crHours.setter
    def crHours(self, cr):
        self.__crHours = cr
        
    # methods to create string representation
    def __str__(self):
        displayString = f'{self.__num:s}:{self.__name:s} ({self.__crHours:d} credit hours)\n'
        return displayString

##    # accessor methods to get private attributes    
##    def getNum(self):
##        return self.__num
##    def getName(self):
##        return self.__name
##    def getCrHours(self):
##        return self.__crHours
##
##    # mutator methods to set private attributes
##    def setNum(self, num):
##        self.__num = num
##    def setName(self, name):
##        self.__name = name
##    def setCrHours(self, crHours):
##        self.__crHours = crHours


if __name__ == '__main__':
    c1 = Course()
    print(c1)
    c2 = Course('CIS2531', 'Intro to Python', 4)
    print(c2)
    c3 = Course()
    c3.num = 'CIS2532'
    c3.name = 'Advanced Python'
    c3.crHours = 4
    print(c3.num, c3.name, c3.crHours)
    
