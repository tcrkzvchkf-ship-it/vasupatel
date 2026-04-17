#if/else statements

age = 16

#Also for if statements there needs to be a 4 space gap given in the statment where it prints, it is not optional it is how python reads if statements
#if statements seem to be conditional values and after ever condition given add " : " 
if age >= 18:
    print("You are an adult")
# this is basically a statement witin the if statement where the if statement does not meet the criteria than run this statement
elif age >= 13:
    print("You are a teen")
# else is like the ending statement if all above statements don't stand true than you print this basically
else:
    print("You are a child")



#for loops

fruits = ["apples", "bananas", "pineapple", "grapes"]
for fruit in fruits:
    print(fruit)
# A "for" loop goes through all items or values that you list and it goes through it one by one
for i in range(1,6):
    print(i)
#you are creating a variable which run through the fruits, which is why you are creating the (i)



#While loops

#So unlike a for loop where it goes through only the details you give it, the while loop runs forever
#Make sure to give the count += 1 or else it will keep running forever and you will have to force quit the terminal

count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

print("Done")



#Fizzbuzz challenge ( Interview Challenge)

# What I learned, so to get the mutltiple of something I need a remainder, for me to get the remainder. i need to use the "%" which would need to == 0 
# Which then in turn gives me the correct multiple from the range I have given
# if you need a range from 1-50 or 1-100 always add one more number at the end like so (1,51) or (1,101)
# Also in this challenge I realized that is one number maybe divisble by both numbers than I need to give that statement first and then give the individual statements after or it will not run the other number all together and it will stand true with the first statement as seen in the errors before

for Fizz in range(1,31):
    if Fizz % 3 == 0 and Fizz % 5 == 0:
        print("Fizzbuzz")
    elif Fizz % 5 == 0:
        print("Buzz")
    elif Fizz % 3 == 0:
        print("Fizz")
    else:
        print(Fizz)

# While loop challenge

count = 0 #This is for the counter, it will start at 0
secret = 7 # this is the number we have given for the system to guess and it is hardcoded in so you can pull it in the answer you give
# While loops don't need a value, they can be given True or False a True while loop will run the code below but if you give it false it will count it as false and disrard the code given
while True: 
    guess = int(input("Guess the number = ")) #This will take the guess, always create a new variable for the inputs and then use that in your if/else/elif statements
    count += 1 #This is the amount you can give to count by so if I gave 2 then it will add by 2
    if guess <= 6:
        print("Your number is too low")
    elif guess >= 8:
        print("Your number is too high")
    elif guess == 7:
        print(f"you got it! The number is {secret}") # I am pulling this from the number we hardcoded instead of writing the actual number we can just pull from it since we have already given it
    print(f"Guess counter = {count}")
    break #"break" will kill the while loop







