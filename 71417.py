class Employee:
		
	def __init__(self, name, IDnumber, department, jobtitle):
		self.name = name
		self.IDnumber = IDnumber
		self.department = department
		self.jobtitle = jobtitle		
		
		
	def __str__(self):
		return 'Name: '+ self.name + '\n' + 'ID Number: ' + self.IDnumber + '\n' + 'Department: ' + self.department + '\n' + 'Job Title: ' + self.jobtitle + '\n'
	
	
#The main function
def main():
	my_employee = Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
	print(my_employee)
	
	my_employee = Employee('Mark Jones', '39119', 'IT', 'Programmer')
	print(my_employee)
	
	my_employee = Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')
	print(my_employee)
	
	
main()
