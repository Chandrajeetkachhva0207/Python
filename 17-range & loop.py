# Print the 1 to 5 numbers:-
# for i in range(1,6):
#     print(i)

#print the even number:
# for i in range(0,20,2):
#     print(i)

#print the odd number:
# for i in range(1,20,2):
#     print(i)

#print Countdown from number 10 to 1:
# for i in range(10,0,-1):
#     print(i)

#Loop through list using index:
# items=["pen","book","notebook"]
# for i in range(len(items)):
#     print(i,items[i])

# genreate the employee id:
# for i in range(0,6):
#     print("EMP.",i)

# create year list:
# years=[]
# for y in range(2015,2026):
#     years.append(y)
# print(years)

#print the cities:
# cities=["mumBai","Pune ", "Jalgaon"]
# for i in range(len(cities)):
#     cities[i]=cities[i].strip().title()
#     print(cities)

#print extract last 4 digit
# ids=["emp-12345","emp-98765","emp-56743"]
# for i in range(len(ids)):
#    print(ids[i][-4:])

#nested loop :
# print the prime numbers:-
nums = int(input("Enter the number: "))

if nums <= 1:
    print("Not a prime number")

else:
    for i in range(2, nums):
        if nums % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
        


