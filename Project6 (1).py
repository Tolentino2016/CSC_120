import string

def uniqueWords(file):
    filein = open(file)
    text = filein.read()
    text = text.translate(str.maketrans(string.punctuation,len(string.punctuation)*" "))
    words = text.split()
    un_words = set(words)
    un_lst = list(un_words)
    un_lst.sort()
    return un_lst
        
    
'''
Sample interaction for uniqueWords :-

>>> uniqueWords('text.txt')
['000', '1', '162', '1840', '1853', '1867', '2', '400', '650', '820', 'Accordingly', 'Arabia', 'Atlantic', 'China', 'Co', 'Cunard', 'Eastern', 'Eight', 'English', 'France', 'Given', 'Great', 'Halifax', 'I', 'If', 'In', 'Java', 'Liverpool', 'No', 'Persia', 'Russia', 'Scotia', 'So', 'a', 'ability', 'accident', 'added', 'after', 'all', 'and', 'as', 'assets', 'astonished', 'at', 'be', 'been', 'between', 'biggest', 'burden', 'business', 'by', 'can', 'canceled', 'carrying', 'charter', 'choose', 'company', 'competition', 'condensed', 'conducted', 'craft', 'crossings', 'crowned', 'dealings', 'delay', 'despite', 'details', 'documents', 'eight', 'even', 'ever', 'everyone', 'famous', 'featuring', 'finest', 'for', 'founded', 'four', 'from', 'fully', 'give', 'greater', 'had', 'has', 'have', 'highly', 'horsepower', 'importance', 'in', 'increased', 'industrialist', 'involving', 'is', 'it', 'its', 'just', 'known', 'later', 'letter', 'line', 'lost', 'made', 'mail', 'man', 'management', 'maritime', 'metric', 'more', 'much', 'name', 'navigational', 'no', 'of', 'official', 'one', 'or', 'other', 'others', 'over', 'owned', 'paddle', 'passengers', 'plow', 'postal', 'power', 'preference', 'propellers', 'provoked', 'recent', 'recorded', 'renewed', 's', 'seas', 'seen', 'service', 'shipowner', 'ships', 'shrewd', 'six', 'so', 'speed', 'steamers', 'still', 'strong', 'success', 'successively', 'survey', 'that', 'the', 'these', 'this', 'three', 'to', 'tonnage', 'tons', 'top', 'transoceanic', 'transportation', 'twelve', 'twenty', 'two', 'unaware', 'understand', 'undertaking', 'uproar', 'vessels', 'voyage', 'were', 'wheels', 'whose', 'will', 'with', 'without', 'wooden', 'world', 'years']
'''

def fileAnalysis(file1,file2):
    filein1 = open(file1)
    filein2 = open(file2)
    
    text1 = filein1.read()
    text1 = text1.translate(str.maketrans(string.punctuation,len(string.punctuation)*" "))
    text2 = filein2.read()
    text2 = text2.translate(str.maketrans(string.punctuation,len(string.punctuation)*" "))
    
    words1 = text1.split()
    words2 = text2.split()
    
    fa_set1 = set(words1)
    fa_set2 = set(words2)
    
    #the 5 set operations
    fa_all = fa_set1 | fa_set2
    fa_in_both = fa_set1 & fa_set2
    fa_in_set1 = fa_set1 - fa_set2
    fa_in_set2 = fa_set2 - fa_set1
    fa_symmetric_difference = fa_set1 ^ fa_set2

    fa_all_lst = list(fa_all)
    fa_all_lst.sort()
    
    fa_in_both_lst = list(fa_in_both)
    fa_in_both_lst.sort()
    
    fa_in_set1_lst = list(fa_in_set1)
    fa_in_set1_lst.sort()
    
    fa_in_set2_lst = list(fa_in_set2)
    fa_in_set2_lst.sort()
    
    fa_symmetric_difference_lst = list(fa_symmetric_difference)
    fa_symmetric_difference_lst.sort()

    final_lst = []
    final_lst.append(fa_all_lst)
    final_lst.append(fa_in_both_lst)
    final_lst.append(fa_in_set1_lst)
    final_lst.append(fa_in_set2_lst)
    final_lst.append(fa_symmetric_difference_lst)
    
    return final_lst
    
'''
Sample interaction for fileAnalysis :-

>>> fileAnalysis('first_file.txt','second_file.txt')
[['Jack', 'The', 'be', 'brown', 'candlestick', 'dog', 'fox', 'jump', 'jumps', 'lazy', 'nimble', 'over', 'quick', 'the'], ['over', 'quick', 'the'], ['The', 'brown', 'dog', 'fox', 'jumps', 'lazy'], ['Jack', 'be', 'candlestick', 'jump', 'nimble'], ['Jack', 'The', 'be', 'brown', 'candlestick', 'dog', 'fox', 'jump', 'jumps', 'lazy', 'nimble']]
'''

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        
    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed -=5
    def get_speed(self):
        return self.__speed
        


'''
Sample interaction for Car by calling carTester (provided below) :-

>>> carTester()
car is accelerating: 
Current speed:  5
Current speed:  10
Current speed:  15
Current speed:  20
Current speed:  25

car is braking: 
Current speed:  20
Current speed:  15
Current speed:  10
Current speed:  5
Current speed:  0
'''

def carTester(): # THIS FUNCTION IS PROVIDED AND DOES NOT NEED TO BE CHANGED
    # Create an instance of Car.
    my_car = Car('2008', 'Honda Accord')

    # Accelerate 5 times.
    print('car is accelerating: ')
    for i in range(5):
        my_car.accelerate()
        print ('Current speed: ', my_car.get_speed())
    print()
    
    # Brake 5 times.
    print ('car is braking: ')
    for i in range(5):
        my_car.brake()
        print ('Current speed: ', my_car.get_speed())


class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title
        
    def get_name(self):
        return self.__name 
    def get_id_number(self):
        return self.__id_number 
    def get_department(self):
        return self.__department 
    def get_job_title(self):
        return self.__job_title

    def __str__(self):
        object_str = 'Name: ' + self.__name + '\n'
        object_str += 'ID number: ' + self.__id_number + '\n'
        object_str += 'Department: ' + self.__department + '\n'
        object_str += 'Title: ' + self.__job_title + '\n'
        return object_str

'''
Sample interaction for Car by calling employeeTester (provided below) :-

>>> employeeTester()
Employee 1:
Name: Susan Meyers
ID number: 47899
Department: Accounting
Title: Vice President

Employee 2:
Name: Mark Jones
ID number: 39119
Department: IT
Title: Programmer

Employee 3:
Name: Joy Rogers
ID number: 81774
Department: Manufacturing
Title: Engineer
'''

def employeeTester(): # THIS FUNCTION IS PROVIDED AND DOES NOT NEED TO BE CHANGED
    # Create three instances of Employee
    emp1 = Employee('Susan Meyers', '47899',
                        'Accounting', 'Vice President')
    emp2 = Employee('Mark Jones', '39119',
                        'IT', 'Programmer')
    emp3 = Employee('Joy Rogers', '81774',
                        'Manufacturing', 'Engineer')

    print('Employee 1:')
    print(emp1)
    print()
    print('Employee 2:')
    print(emp2)
    print()
    print('Employee 3:')
    print(emp3)
