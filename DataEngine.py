import re
import json

class DataEngine:
	def __init__(self, file):
		self.file = file
		
		with open ("regex.json","r") as file:
				self.regex = json.load(file)

		self.temp_storage = []
		self.email_storage = []
		self.phone_storage = []
		
	def scan(self):
		with open (self.file,"r") as file:
			for line in file:
				self.temp_storage.append((line.strip()))

	# the id function is correctly capturing lines where the regex patterns are matched.
	# the id function is failing to split that line and only return the correct pattern.
	# Instead, the entire line is added to the storage list and erroneous data is displayed 
	# in the extracted list.


	def id(self):
		for line in self.temp_storage:
			email_match = re.search(self.regex["email_extract_pattern"],line)
			phone_match = re.search(self.regex["uk_phone_extract_pattern"],line)
			if email_match:
				self.email_storage.append(line)
			elif phone_match:
				self.phone_storage.append(line)
			else:
				print (f"Value Invalid: {line}")

		

	def extract(self):
		print("\nExtracted list:")		
		for line in self.email_storage:
			print(line)
		
		for line in self.phone_storage:
			print(line)
		

	def display(self):
		pass


p1 = DataEngine("data.txt")
p1.scan()
p1.id()
p1.extract()

# Test: printing one of my regex commands from the json file
#print(p1.regex["email_extract_pattern"])

