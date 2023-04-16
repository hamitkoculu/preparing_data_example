#Open the file in read mode
file = open("C:/Users/Hamit/Desktop/employee_revenue.txt", "r")
data = file.read()

#Seperate the data into lines
lines = data.splitlines()
'''print(lines)'''

#Take the first line
string = lines[0]
'''print(string)'''

#Remove the whitespaces from the edges
string = string.strip(" ")
'''print(string)'''

#Convert the string to lowercase
string = string.lower()
'''print(string)'''

#Capitalize the first character
string = string.capitalize()
'''print(string)'''

#Split the sentence into words
split_string = string.split()
'''print(split_string)'''

#Use the index 0 to access the name element
name = split_string[0]
'''print(name)'''

#Use the index 2 to access the number of calls element
call_number = split_string[2]
'''print(call_number)'''

#Find the element with the "$" sign
for i in split_string:
    #Divide the number from it
    if "$" in i:
        average_deal_size = i.split("$")[0]
#Print the average deal size 
'''print(average_deal_size)'''

#Find the index of elements "dollars"
dollar_index = split_string.index("dollars")
'''print(dollar_index)'''

#Subtract one from the index to identify the index of the revenue element
revenue_index = dollar_index - 1
'''print(revenue_index)'''

#Extract the revenue
revenue = split_string[revenue_index]
'''print(revenue)'''

#Convert the datatypes of average deal size, number of calls, and revenue
average_deal_size = int(average_deal_size)
call_number = int(call_number)
revenue = int(revenue)

#Print out the extracted information
'''print('Name:', name)
print('Number of calls:', call_number)
print('Average deal size:', average_deal_size)
print('Revenue:', revenue)
'''
#Create empty list for the names, number of calls, average deal sizes, revenues
names = []
call_numbers = []
average_deal_sizes = []
revenues = []

#Define a function to clean and extract the data
def clean_extract(lines):

    #Loop over the whole data
    for employee in lines:
        #Clean the string
        employee = employee.strip(" ")
        employee = employee.lower()
        employee = employee.capitalize()

        #Split the clean string
        split_employee = employee.split(" ")

        #Extract the name
        name = split_employee[0]
        call_number = split_employee[2]

        #Extract the average deak size
        for i in split_employee:
            if "$" in i:
                average_deal_size = i
        average_deal_size = average_deal_size.split("$")[0]

        #Extract the revenue
        dollar_index = split_employee.index("dollars")
        revenue_index = dollar_index - 1
        revenue = split_employee[revenue_index]

        #Convert to the correct data types
        average_deal_size = int(average_deal_size)
        call_number = int(call_number)
        revenue = int(revenue)

        #Append the information to the lists
        names.append(name)
        call_numbers.append(call_number)
        average_deal_sizes.append(average_deal_size)
        revenues.append(revenue)

    return names, call_numbers, average_deal_sizes, revenues

#Assign returned values to variables
names, call_numbers, average_deal_sizes, revenues = clean_extract(lines)

#Print out the information
print("Names:", names)
print("Number of calls:", call_numbers)
print("Average deal sizes:", average_deal_sizes)
print("Revenues:", revenues)

#Check the number of employees
'''print(len(names))'''

#Generate IDs
IDs = list(range(0,11))
'''print(IDs)'''

#Pair the names with IDs in a dictionary
dictionary1 = dict(zip(IDs, names))
'''print(dictionary1)'''

#Pair the names with the revenues
dictionary2 = dict(zip(revenues, names))
'''print(dictionary2)'''

#Find the lowest performing employees (ascending order)
sorted_dictionary = sorted(dictionary2)[0:3]
for i in sorted_dictionary:
    '''print(dictionary2[i])'''

#Find the best performing employees (descending order)
sorted_dictionary = sorted(dictionary2, reverse=True)[0:3]
for i in sorted_dictionary:
    '''print(dictionary2[i])'''
