# Email Extracter.
# Uses regex commands stored in regex.json
# to search for key data within an input
# such as a document or scraped data, etc. 

import json
import re

with open("regex.json", "r") as file:
    regex_bank = json.load(file)

email_regex = regex_bank["email_extract_pattern"]

user_input = "us_er.he5638llo-test@gmail.com"
if re.match(email_regex, user_input):
    print("email found")