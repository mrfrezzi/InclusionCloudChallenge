# Question 5
import json
import datetime
import os

# Question 5 - Read in the document from a file
# JSON file should be placed in the Desktop
json_full_path = 'C:/Users/' + os.environ.get('USERNAME') + '/Desktop/JsonChallenge.json'
json_file = open(json_full_path)
json_data = json.load(json_file)
json_file.close()

# Question 5 - Find and print The Payee ID value
# Assumptions: payee and payee/id exist in Json file, with the same hierarchy provided in the challenge
json_payeeID = json_data['payee']['id']
# some validations....
# print (json_payeeID)


# Question 5 - Any invoices that contain the text “583”
# Assumptions: invoiceIds exists in Json file, , with the same hierarchy provided in the challenge
json_filtered_invoices = [invoice for invoice in json_data['invoiceIds'] if '583' in invoice]
# some validations....
# print (json_filtered_invoices)

# Question 5 - Change any date/time fields to text in the format ‘%Y-%m-%dT%H:%M:%S’
# Assumptions: DateTime fields must contain 'DateTime' in the field name
datetime_fields = [field for field in json_data if 'DateTime' in field]
for field in datetime_fields:
    datetime_obj = datetime.datetime.fromtimestamp(json_data[field] / 1e3)
    json_data[field] = datetime_obj.strftime('%Y-%m-%dT%H:%M:%S')
# some validations....
# print (json_data['fileDateTime'])
# print (json_data['receivedDateTime'])
# print (json_data['claimDateTime'])


# Question 5 - Write the json document back out to a new file
# New file will be created in the Desktop
new_json_full_path = 'C:/Users/' + os.environ.get('USERNAME') + '/Desktop/JsonChallenge ' + datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S') + '.json'
new_json_file = open(new_json_full_path, 'w')
json.dump(json_data,new_json_file, indent= 2)

