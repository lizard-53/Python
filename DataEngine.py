import re
import json

class DataEngine:
	def __init__(self, data_file):
		self.file = data_file
		
		with open ("regex.json","r") as json_file:
				self.regex = json.load(json_file)

		self.email_storage = []
		self.phone_storage = []


	def parse_file(self):
		with open (self.file,"r") as data_file:
			for line in data_file:
				email_match = re.findall(self.regex["email_extract_pattern"],line)
				phone_match = re.findall(self.regex["uk_phone_extract_pattern"],line)

				if email_match:
					self.email_storage.extend(email_match)
				if phone_match:
					self.phone_storage.extend(phone_match)

		print("\nExtracted list:")		
		for line in self.email_storage:
			print(line)	
		for line in self.phone_storage:
			print(line)

p1 = DataEngine("data.txt")
p1.parse_file()