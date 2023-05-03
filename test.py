"""
number = int(input("I'll count odd numbers until the numnber you'll give: "))
for i in range(1, number, 2):
    print(i)
    """

""" 
## for lopp the given times table 
times_table = int(input("Enter a number you want me to display its times table:"))

## use a for loop to display the times table from 1 to 12
for i in range(1,13):
    print(times_table, 'x', i, '=', times_table * i)5
 """

"""
## while loop for password
password = 'let me in'

entry = input('Please enter your password:')

while entry != password:
    print('wrong password. Please try again')
    entry = input('Please entre your password:')
print('Welcome, password accepted.')   
""" 

"""
## initialise a total variable
total = 0
while True:
    number = int(input('Enter a number, or 0 to stop:'))
    if number ==0:
        break
    total+=number

    print('The Total is:', total)
"""

"""
no1 = int(input('Enter the first number: '))
no2 = int(input('Enter the second number: '))
if no1>no2:
    print('The first number is greater than the second number.')
else:    
    print('The second number is greater than the first number.')

large_no = max(no1, no2)
print('the largest number is:', large_no)
"""

"""
## write a program to determine if someone is eligible to enter a pub
age = int(input('What is your age?'))
if age >=18:
    print('Welcome to the pub! Drink responsibly.')
elif age >=13:
    print('You are too young to enter on your own. You must ride with an adult.')
else: 
    print('Common mate! Go home and do the chores for mama.')
"""

"""
## getting the year the user was born
year = int(input('What year were you born?'))

if year % 4 == 0:
    print('you were born in a leap year.')
else:
    print('you were not born in a leap year.')
"""

x = 1
y = 1
if x ==1 and y ==1:
    print('x is 1')
    print('y is 1')
elif x ==1 and y != 1:
    print('x is 1')
    print('y is something else')
elif x !=1 and y ==1:
    print('x is something else')
    print('y is 1')
else:
    print('x is something else')
    print('y is something else')
