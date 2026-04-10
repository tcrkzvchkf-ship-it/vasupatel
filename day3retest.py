#Challege 1:

grade = int(input("Check your current grade level = "))
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
elif grade < 60:
    print ("F")
print(f"Your current level is {grade}")


#Challege 2:

count = 10

while count > 0:
    print(count)
    count -= 1
print ("Blast off")



#Challege 3:

for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("Vasu")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)