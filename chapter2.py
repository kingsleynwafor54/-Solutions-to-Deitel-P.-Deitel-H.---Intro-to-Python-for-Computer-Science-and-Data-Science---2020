


# # name=['Lagos','Ibadan']
# # location=['Nigeria','Songo']
# # Animal=['goat','Pig']
# # # zipped= zip(name,location,Animal)

# # # print(list(zipped))

# # for i,j,k in zip(name,location,Animal):
# #     print(f'{i} is a city in {j} and {k} is the favorite animal in {j}')

# # # vowels list
# # vowels = ['e', 'a', 'u', 'o', 'i']

# # # sort the vowels
# # vowels.sort()

# # # print vowels
# # print('Sorted list:', vowels)
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # print("Original list of integers:")
# # print(nums)
# # print("\nSquare every number of the said list:")
# # square_nums = list(map(lambda x: x ** 2, nums))
# # print(square_nums)
# # print("\nCube every number of the said list:")
# # cube_nums = list(map(lambda x: x ** 3, nums))
# # print(cube_nums)

# x=2
# y=3

# print((x + y), '=', (y + x))


# # grade=int(input('Enter your grade'))

# # if grade>=90:
# #     print(f'congratulations you grade of {grade} has gotten an A')


# # .5 (Circle Area, Diameter and Circumference) For a circle of radius 2, display the diameter, circumference and area. Use the value 3.14159 for π. Use the following formulas
# # (r is the radius): diameter = 2r, circumference = 2πr and area = πr2. [In a later chapter, we’ll
# # introduce Python’s math module which contains a higher-precision representation of π.]
# from math import pi
# radius=2
# diameter=2*radius
# circumference = 2*pi*radius
# area = pi*radius**2

# print(f'radius={radius} diameter={diameter} circumference={circumference} area={area}')

# """
# 2.6 (Odd or Even) Use if statements to determine whether an integer is odd or even.
# [Hint: Use the remainder operator. An even number is a multiple of 2. Any multiple of 2
# leaves a remainder of 0 when divided by 2.]
# """
# number=int(input('Enter a number\n'))
# if number%2==0:
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an odd2 number")


# '''
# 2.7 (Multiples) Use if statements to determine whether 1024 is a multiple of 4 and
# whether 2 is a multiple of 10. (Hint: Use the remainder operator.)'''

# if 1024%4==0 and 10%2==0:
#     print(f'1024 and 10 are multiples of 4 and 2 respectively')
# '''
# 2.8 (Table of Squares and Cubes) Write a script that calculates the squares and cubes
# of the numbers from 0 to 5. Print the resulting values in table format, as shown below. Use
# the tab escape sequence to achieve the three-column output.'''

# print(f'number        square    cube')
# print(f'  {0:<2}             {0**2:<3}     {0**3:<2}')
# print(f'  {1:<2}             {1**2:<3}     {1**3:<2}')
# print(f'  {2:<2}             {2**2:<3}     {2**3:<2}')
# print(f'  {3:<2}             {3**2:<3}     {3**3:<2}')
# print(f'  {4:<2}             {4**2:<3}     {4**3:<2}')
# print(f'  {5:<2}             {5**2:<3}     {5**3:<2}')

# print(f'number  square  cube')
# for i in range(6):
#     if i>=4:
#         print(f'{i}       {i**2}       {i**3}')
#     else:
#          print(f'{i}       {i**2}        {i**3}')

# print(ord('B'))
# print(ord('C'))
# print(ord('D'))
# print(ord('b'))
# print(ord('c'))
# print(ord('d'))
# print(ord('0'))
# print(ord('1'))
# print(ord('2'))
# print(ord('$'))
# print(ord('*'))
# print(ord('+'))

'''2.10 (Arithmetic, Smallest and Largest) Write a script that inputs three integers from
the user. Display the sum, average, product, smallest and largest of the numbers. Note that
each of these is a reduction in functional-style programming. '''

# num1=int(input('Enter your number'))
# num2=int(input('Enter your number'))
# num3=int(input('Enter your number'))
# sum=num1+num2+num3
# average=sum/3
# product=num1*num2*num3
# smallest=num1
# if num2<smallest:
#     smallest=num2
# if num3<smallest:
#     smallest=num3

# largest=num1
# if num2>largest:
#     largest=num2
# if num3>largest:
#     largest=num3

# print(f'sum={sum} average={average} product={product} smallest={smallest} largest={largest}')


# 2.11 (Separating the Digits in an Integer) Write a script that inputs a five-digit integer
# from the user. Separate the number into its individual digits. Print them separated by three
# spaces each. For example, if the user types in the number 42339, the script should print 
# 4 2 3 3 9
# Assume that the user enters the correct number of digits. Use both the floor division and
# remainder operations to “pick off” each digit.

# number=42339
# num1=number//10000
# num2=number//1000%10
# num3=number//100%10
# num4=number//10%10
# num5=number%10
# print(f'{num1} {num2} {num3} {num4} {num5}')

'''
2.12 (7% Investment Return) Some investment advisors say that it’s reasonable to expect a 7% return over the long term in the stock market. Assuming that you begin with
$1000 and leave your money invested, calculate and display how much money you’ll have
after 10, 20 and 30 years. Use the following formula for determining these amounts:
a = p(1 + r)
n
where
p is the original amount invested (i.e., the principal of $1000),
r is the annual rate of return (7%),
n is the number of years (10, 20 or 30) and
a is the amount on deposit at the end of the nth year.'''
# p=1000
# r=0.007
# n1=10
# n2=20
# n3=30
# a1=p*(1+r)**n1
# a2=p*(1+r)**n2
# a3=p*(1+r)**n3
# print(f'10years_profit={a1} 20years_profit={a2} 30years_profit={a3}')

# value=100000000000000000**100000000000000
# print(value)

'''
2.14 (Target Heart-Rate Calculator) While exercising, you can use a heart-rate monitor
to see that your heart rate stays within a safe range suggested by your doctors and trainers.
According to the American Heart Association (AHA) (http://bit.ly/AHATargetHeart-Rates), the formula for calculating your maximum heart rate in beats per minute is 220
minus your age in years. Your target heart rate is 50–85% of your maximum heart rate.
Write a script that prompts for and inputs the user’s age and calculates and displays the
user’s maximum heart rate and the range of the user’s target heart rate. [These formulas
are estimates provided by the AHA; maximum and target heart rates may vary based on
the health, fitness and gender of the individual. Always consult a physician or qualified
healthcare professional before beginning or modifying an exercise program.]'''

# age=int(input('Enter your age'))
# maximum_heart_rate=220-age
# target_heart_rate1=0.5*maximum_heart_rate
# target_heart_rate2=0.85*maximum_heart_rate
# print(f'maximum_heart_rate {maximum_heart_rate}\ntarget_heart_rate_range from {target_heart_rate1} to {target_heart_rate2}')

'''
2.15 (Sort in Ascending Order) Write a script that inputs three different floating-point
numbers from the user. Display the numbers in increasing order. Recall that an if statement’s suite can contain more than one statement. Prove that your script works by running it on all six possible orderings of the numbers. Does your script work with duplicate
numbers? [This is challenging. In later chapters you’ll do this more conveniently and with
many more numbers.'''

# num1=float(input('Enter your number'))
# num2=float(input('Enter your number'))
# num3=float(input('Enter your number'))
# # # Here you find the smallest number first
# smallest=num1
# if num2<smallest:
#     smallest=num2
# if num3<smallest:
#     smallest=num3

# # # Here you find the largest number 
# largest=num1
# if num2>largest:
#     largest=num2
# if num3>largest:
#     largest=num3

# sum=num1+num2+num3
# #Here you find the secondsmallest number

# print(f'{smallest} {sum-smallest-largest} {largest}')


# from decimal import Decimal
# x=Decimal('10.5')
# y=Decimal('2')
# print(x+y)
# a = b = 7
# print('a =', a, '\nb =', b) 

# number=1234321
# num=number
# palindrome=''
# while number>0:
#     pn=number%10
#     palindrome+=str(pn)
#     number//=10
    
# if int(palindrome)==num:
#     print(f'{num} is a palindrome')
# else:
#     print(f'{num} is not palindrome')


# number=1234556789045656787898900
# tens=len(str(number))-1
# num=tens
# py=number//10**tens
# py=str(py)
# while num>0:
#     tens-=1
#     pn=number//10**tens%10
#     py+=" "+str(pn)
#     num-=1
    
# print(py)

number=6
for i in range(1,number):
    number*=i

print(number)

grades=[1,2,18,4,3,17,5,19,20,28]
largestnumber=grades[0]
secondlargestnumber=grades[0]
for i in range(len(grades)):
    for j in range(len(grades)):
        if grades[j]>largestnumber:
            largestnumber=grades[j]       
        elif grades[j] > secondlargestnumber and grades[j] < largestnumber:
            secondlargestnumber=grades[j]
print(f'largest_number {largestnumber} second_largest_number {secondlargestnumber}')



largestnumber1=grades[0]
secondlargestnumber1=grades[0]
grades=[1,2,18,4,3,21.5,17,5,19,20,28]
for i in range(len(grades)):
    if grades[i]>largestnumber1:
        secondlargestnumber1=largestnumber1
        largestnumber1=grades[i]
    elif grades[i]>secondlargestnumber1:
        secondlargestnumber1=grades[i]

print(f'largest_number {largestnumber1} second_largest_number {secondlargestnumber1}')
        

# for i in range(10):
#     print('*'*i)
# print()
# for i in range(10,0,-1):
#     print('*'*i)

# print()
# for i in range(10,0,-1):
#     print(f"{'*'*i:>10}")

# print()
# for i in range(10):
#     print(f"{'*'*i:>10}")


# i=1
# for j in range(10,0,-1):
#         print(f"{'*'*i:<10}  {'*'*j:<10} {'*'*j:>10}  {'*'*i:>10}" ) 
#         i+=1
j=12
for i in range(1,11):
    j-=1
    for k in range(j,0,-1):
        print(f"{'*'*i:<10}  {'*'*k:<11}   {'*'*k:>14}  {'*'*i:>10}" )
        break
        

        

           
