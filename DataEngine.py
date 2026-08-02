import re
import json
import sys
import pandas as pd


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

		email_col = pd.Series(self.email_storage, name="Email Addresses")
		phone_col = pd.Series(self.phone_storage, name="UK Phone Numbers")
		df = pd.concat([email_col, phone_col], axis=1)

		output_file_path = "extracted_data_list.xlsx"

		with pd.ExcelWriter(
			output_file_path,
			engine="xlsxwriter",
			engine_kwargs={"options": {"strings_to_numbers": False}},
		) as writer:
			df.to_excel(writer, index=False, sheet_name="Contacts")

		print("\nData successfully saved to extracted_data_list.xlsx")


def main():
	if len(sys.argv)==2:
		data_file = sys.argv[1]
	else:
		data_file = (input(f"Enter file name: "))

	try:
		p1 = DataEngine(data_file)
		p1.parse_file()
	except FileNotFoundError:
		print(f"Error: The file {data_file} could not be found.")
		main()
	except Exception as e:
		print(f"An unexpected error occured: {e}")

if __name__ == "__main__":
	main()