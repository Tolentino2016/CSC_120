#Chapter 5 Programming Exercises:
#7
def stadium_seating():
    a = int(input('How many Class A seats: '))
    b = int(input('How many Class B seats: '))
    c = int(input('How many Class C seats: '))
    total = (a * 20) + (b * 15) + (c * 10)
    print('Total amount of ticket sales $', total, sep='')


def jobEstimate():
    wall_space = int(input('Enter square feet of wall space to be painted:'))
    paint_price = int(input('Enter price of paint per gallon:'))
    paint_gallon = wall_space / 112
    req_labor = paint_gallon * 8
    cost_paint = paint_price * paint_gallon
    labor_charge = req_labor * 35
    total = cost_paint + labor_charge
    print(format(paint_gallon,'.2f'),'gallons of paint are required for the paint job')
    print(format(req_labor,'.2f'),'hours of labor are required for the paint job')
    print('The cost of paint is $', format(cost_paint,'.2f'), sep='')
    print('The labor charge is $', format(labor_charge,'.2f'), sep='')
    print('The total cost of the paint job is $', format(total,'.2f'), sep='')


def calc_average(score1, score2, score3, score4, score5):
        score = (score1 + score2 + score3 + score4 + score5)/5
        return score

def determine_grade(score):
        if 90 <= score <= 100:
            return 'A'
        elif 80 <= score <= 89:
            return 'B'
        elif 70 <= score <= 79:
            return 'C'
        elif 60 <= score <= 69:
            return 'D'
        else:
            return 'F'

def lineNumbers():
    filename = input('Enter file name: ')
    fileout = open(filename,'r')
    for line in fileout:
        print('1:',line)
       


def sumNumbers():
    file = open('numbers.txt','r')
    total = 0
    for line in file:
        num = int(line)
        total += num
    print(total)
    file.close()
    
    
    
        
