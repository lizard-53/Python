import re
import json

class DataEngine:
	def __init__(self, data_file):
		self.file = data_file
		
		with open ("regex.json","r") as json_file:
				self.regex = json.load(json_file)

		self.temp_storage = []
		self.email_storage = []
		self.phone_storage = []
		
	def scan(self):
		with open (self.file,"r") as data_file:
			for line in data_file:
				self.temp_storage.append((line.strip()))

	def id(self):
		for line in self.temp_storage:
			email_match = re.search(self.regex["email_extract_pattern"],line)
			phone_match = re.search(self.regex["uk_phone_extract_pattern"],line)

			if email_match:
				self.email_storage.append(email_match.group())
			if phone_match:
				self.phone_storage.append(phone_match.group())
			
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