import json

# Define JSON string
jsonString = '{ "id": 121, "name": "Naveen", "course": "MERN Stack"}'
 
# Convert JSON String to Python
student_details = json.loads(jsonString)
 
# Print Dictionary
print(student_details)
 
# Print values using keys
print(student_details['name'])
print(student_details['course']) 

#converting json file to python object

with open('json data.json') as json_file:
    data = json.load(json_file)
 
    # Print the type of data variable
    print("Type:", type(data))
 
    # Print the data of dictionary
    print("\nPeople1:", data['people1'])