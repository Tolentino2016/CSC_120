class Car:
		
	def __init__(self, year, make):
		self.__year_model = year
		self.__make = make
		self.__speed = 0
		
	def accelerate(self):
		self.__speed +=5		
		
	
	def brake(self):
		self.__speed -=5
		
		
	def get_speed(self):
		return self.__speed
	
	
#The main function
def main():
	my_car = Car('2001', 'Durango')
	
	for i in range(1, 6):
		my_car.accelerate()
		print(my_car.get_speed())
		
		
	for i in range(1, 6):
		my_car.brake()
		print(my_car.get_speed())

main()
