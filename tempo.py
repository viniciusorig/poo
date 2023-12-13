class tempo:
	def __init__(self, hour=0, minute=0, second=0):
		self.hour = hour
		self.minute = minute
		self.second = second

	def __repr__(self):
		return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

	def __add__(self, outro:'tempo'):
		second = self.second + outro.second
		minute = self.minute + outro.minute
		hour = self.hour + outro.hour
		if(second >= 60):
			minute = minute + 1
			second = second - 60
		if(minute >= 60):
			hour = hour + 1
			minute = minute - 60
		if(hour >=24):
			hour = hour - 24
		return tempo(hour, minute, second) 
    
	def __sub__(self, outro:'tempo'):
		second = self.second - outro.second
		minute = self.minute - outro.minute
		hour = self.hour - outro.hour
		if(second < 0):
			minute = minute - 1
			second = second + 60
		if(minute < 0):
			hour = hour - 1
			minute = minute + 60
		if(hour < 0):
			hour = hour + 24
		return tempo(hour, minute, second) 
	
	def __lt__(self, outro:'tempo'):
		
		if(self.hour < outro.hour):
			return True
		elif(self.hour > outro.hour):
			return False
			
			
		if(self.minute < outro.minute):
			return True
		elif(self.minute > outro.minute):
			return False
			
			
		if(self.second < outro.second):
			return True
		elif(self.second > outro.second):
			return False
			
		return "igual"
		
	def __gt__(self, outro:'tempo'):
		
		if(self.hour > outro.hour):
			return True
		elif(self.hour < outro.hour):
			return False
			
			
		if(self.minute > outro.minute):
			return True
		elif(self.minute < outro.minute):
			return False
			
			
		if(self.second > outro.second):
			return True
		elif(self.second < outro.second):
			return False
		
		return "igual"

	def __le__(self, outro:'tempo'):
		
		if(self.hour <= outro.hour):
			return True
		elif(self.hour > outro.hour):
			return False
			
			
		if(self.minute <= outro.minute):
			return True
		elif(self.minute > outro.minute):
			return False
			
			
		if(self.second <= outro.second):
			return True
		elif(self.second > outro.second):
			return False
			
	def __ge__(self, outro:'tempo'):
		
		if(self.hour >= outro.hour):
			return True
		elif(self.hour < outro.hour):
			return False
			
			
		if(self.minute >= outro.minute):
			return True
		elif(self.minute < outro.minute):
			return False
			
			
		if(self.second >= outro.second):
			return True
		elif(self.second < outro.second):
			return False
	
	def __eq__(self, outro:'tempo'):
		if(self.hour == outro.hour and self.minute == outro.minute and self.second == outro.second):
			return True
		else:
			return False
	
		def __ne__(self, outro:'tempo'):
			if(self.hour != outro.hour and self.minute != outro.minute and self.second != outro.second):
				return True
			else:
				return False
	
	
tempo1 = tempo(23, 30, 45)
tempo2 = tempo(1, 45, 15)

print(tempo1)
print(tempo2)
print(tempo1 + tempo2)
print(tempo1 - tempo2)
print(tempo1 < tempo2)
print(tempo1 > tempo2)
print(tempo1 <= tempo2)
print(tempo1 >= tempo2)
print(tempo1 == tempo2)
print(tempo1 != tempo2)

