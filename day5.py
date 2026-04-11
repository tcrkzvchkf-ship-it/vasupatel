# Lists and Dictionaries

fruits = ["apple", "banana", "mango", "grape", "orange"]

print(fruits[0]) # prints the first item 
print(fruits[-1]) #prints the last item
print(fruits[1:3]) #prints the items at index 1 and 2 (banana & mango) the list starts at 0,1,2,3,4,5 and so and so forth so here it woudl call the second name and the third name on that list!

fruits.append("kiwi") #adds to the end of the list
fruits.remove("banana") #remove by value
print(len(fruits)) #prints(len) is used ot count out how items there are in the list that you create in this example "fruits"
#the for loop is created to print out all the names in the list quicker instead of writing each print statement out for a single fruit you can just a for loop and print out the list

for fruit in fruits:
    print(fruit)




#List comprehensions:

numbers = [1,2,3,4,5,6,7,8,9,10]

squared = [n * n for n in numbers] # this is going through each number and multiplying it by the same number and going through the whole list and getting the square root of all numebrs in the list and printing it back out by calling at the bottom using print
even = [n for n in numbers if n % 2 == 0] #this is checking for all numbers divsible by 2

print(squared) # printing out the sqaured numbers
print(even) # printing even numbers


#Dictionaries:

person = {
    "name": "Vasu",
    "age": 26,
    "city": "Orlando",
    "is_student": False
}

print(person["name"])
print(person["age"])

person["job"] = "Software Engineer"
person["age"] = 27
del person["is_student"]

for key, value in person.items():
    print(f"{key}: {value}")

#Challenge contact book:

def show_all(contact):
    for key, value in contact.items():
        print(f"{key}: {value}")


def add_contact(contact, name, phone, email):
    contact[name]= {"phone": phone, "email": email}

    

def find_contact(contact,name):
    if name in contact:
        print(contact[name])
    else:
        print("Contact not found!")

contact = {
    "Vasu": {"phone": "123-456-7899", "email": "vasu@gamil.com"},
    "Alex": {"phone": "457-739-9573", "email": "alex@gamil.com"},
    "Piyu": {"phone": "678-142-0932", "email": "piyu@gamil.com"}
}

show_all(contact)
add_contact(contact, "raj", "563-475-5839", "raj@gmail.com")
show_all(contact)
find_contact(contact, "Vasu")
