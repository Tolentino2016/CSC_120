#problem 1

def problem1():
    file = open('charge_accounts.txt')
    line = file.readlines()
    accounts = []
    for num in line:
        num = num.rstrip('\n')
        accounts.append(num)
    account_number = input('Enter a charge account number: ')
    if account_number in accounts:
        print('Account number', account_number, 'is valid.')
    else:
        print('Account number', account_number, 'is not valid.')
            
    



#problem 2

def problem2():
    ans_lst = []
    for i in range(20):
        answers = input('Enter your answer(uppercase letter): ')
        ans_lst.append(answers)
    stu_sol = open('student_solution.txt','w')
    for x in ans_lst:
        stu_sol.write(x + '\n')
        
    cor_lst = []
    cor_ans = open('correct_answers.txt')
    for k in cor_ans:
        k = k.rstrip('\n')
        cor_lst.append(k)
    print(ans_lst)
    print(cor_lst)
    print('-------------------------------------')
    
    correct = 0
    incorrect = 0
    
    index = 0
    incorrect_list = []
    for line in cor_lst:
        if line == ans_lst[index]:
            correct += 1
            index += 1 
        else:
            i = ans_lst[index]
            incorrect_list.append(i)
            incorrect += 1
            index += 1
    
    if correct >= 15:
        print('Congratulations!! You passed the exam.')
    else:
        print('Sorry, you did not pass the exam.')
    
    print('Number of questions you answered correctly:', correct)
    print('Number of questions you answered incorrectly:', incorrect)
    print('Questions you answered incorrectly:', incorrect_list)
    
    
        

#problem 3

def problem3():
    text_2 = ""
    text = input("Enter a string: ")
    x = 0
    for i in text:
        if i.isupper() and x > 0:
            text_2 = text_2 + " " + i.lower()
        else:
            text_2 += i
        x += 1
    #first_letter_capitalize = text.upper()
    #new_text = first_letter_capitalize[0]
    print(text_2)            
    
