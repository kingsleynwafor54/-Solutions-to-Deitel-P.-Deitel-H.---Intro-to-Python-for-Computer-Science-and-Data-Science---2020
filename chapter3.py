'''
3.1 (Validating User Input) Modify the script of Fig. 3.3 to validate its inputs. For any
input, if the value entered is other than 1 or 2, keep looping until the user enters a correct

value. Use one counter to keep track of the number of passes, then calculate the number
of failures after all the user’s inputs have been received.'''
# passed=0
# failed=0
# pin=True
# while pin :
#     value=int(input('Enter you number'))
#     if value>=50:
#         passed+=1
#     else:
#         failed+=1
#     if value==2 or value==1:
#         failed-=1
#         pin=False
  
# print(f'passed={passed} failed={failed}')

'''
3.6 (Turing Test) The great British mathematician Alan Turing proposed a simple test
to determine whether machines could exhibit intelligent behavior. A user sits at a computer and does the same text chat with a human sitting at a computer and a computer operating by itself. The user doesn’t know if the responses are coming back from the human
or the independent computer. If the user can’t distinguish which responses are coming
from the human and which are coming from the computer, then it’s reasonable to say that
the computer is exhibiting intelligence. 
Create a script that plays the part of the independent computer, giving its user a simple medical diagnosis. The script should prompt the user with 'What is your problem?'
When the user answers and presses Enter, the script should simply ignore the user’s input,
then prompt the user again with 'Have you had this problem before (yes or no)?' If
the user enters 'yes', print 'Well, you have it again.' If the user answers 'no', print
'Well, you have it now.'
Would this conversation convince the user that the entity at the other end exhibited
intelligent behavior? Why or why not?'''

# user_response=input('What is your problem?')
# print('Have you had this problem before?')
# user_response1=input('Enter your response(YES OR NO)')
# user_response_to_lowercase=user_response1.lower()
# if user_response_to_lowercase== 'yes':
#     print('Well, you have it again')
# else:
#     print("Well, you have it now")

'''
3.7 (Table of Squares and Cubes) In Exercise 2.8, you wrote a script to calculate the
squares and cubes of the numbers from 0 through 5, then printed the resulting values in
table format. Reimplement your script using a for loop and the f-string capabilities you
learned in this chapter to produce the following table with the numbers right aligned in
each column.
 Exercises 113
number square cube 
 0       0      0
 1       1      1
 2       4      8
 3       9     27
 4      16     64
 5      25    125'''
# print(f'number        square    cube')
# for i in range(6):
#     print(f'  {i:<2}             {i**2:>3}     {i**3:>2}')
'''
Arithmetic, Smallest and Largest) In Exercise 2.10, you wrote a script that input
three integers, then displayed the sum, average, product, smallest and largest of those values. Reimplement your script with a loop that inputs four integers.
'''
# grades=[1,2,18,4,3,21.5,17,5,19,20,28]
# largestnumber1=grades[0]
# smallest_number=grades[0]
# total=0
# product=1
# average=0
# for i in range(len(grades)):
#     if grades[i]>largestnumber1:
#         largestnumber1=grades[i]

#     if grades[i]<smallest_number:
#         smallest_number=grades[i]
#     total+=grades[i]
#     product*=grades[i]

# print(f'sum{total} average={total//len(grades)} product={product} smallest_number={smallest_number} largest_number{largestnumber1}')
'''
 (Separating the Digits in an Integer) In Exercise 2.11, you wrote a script that separated a five-digit integer into its individual digits and displayed them. Reimplement your
script to use a loop that in each iteration “picks off” one digit (left to right) using the //
and % operators, then displays that digit. '''

# number=1234556789045656787898900
# tens=len(str(number))-1
# num=tens
# py=number//10**tens
# separated_numbers=str(py)
# while num>0:
#     tens-=1
#     pn=number//10**tens%10
#     separated_numbers+=" "+str(pn)
#     num-=1   
# print(separated_numbers)

'''
3.10 (7% Investment Return) Reimplement Exercise 2.12 to use a loop that calculates
and displays the amount of money you’ll have each year at the ends of years 1 through 30.'''
# from decimal import Decimal
# principal=Decimal(input('Enter your amount'))
# compound_interest=Decimal(0.0)
# rate=Decimal(7/100)
# for year in range(1,31):
#     compound_interest=principal*(1+rate)**year
#     print(f'Compound interest for the year{2022+year}={compound_interest:>10.2f}')
"""
3.11 (Miles Per Gallon) Drivers are concerned with the mileage obtained by their automobiles. One driver has kept track of several tankfuls of gasoline by recording miles driven
and gallons used for each tankful. Develop a sentinel-controlled-repetition script that
prompts the user to input the miles driven and gallons used for each tankful. The script
should calculate and display the miles per gallon obtained for each tankful. After processing all input information, the script should calculate and display the combined miles per
gallon obtained for all tankfuls (that is, total miles driven divided by total gallons used)"""

# miles_per_gallon=0
# pin=True
# while pin :
#     gallon=float(input('Enter the gallons used'))
#     mile=float(input('Enter miles driven'))
#     if gallon==-1:
#         pin=False
#     miles_per_gallon=abs(mile/gallon)
#     print(f'The  mile/gallon for this tank was {miles_per_gallon:>10.6}')

'''
3.12 (Palindromes) A palindrome is a number, word or text phrase that reads the same
backwards or forwards. For example, each of the following five-digit integers is a palindrome: 12321, 55555, 45554 and 11611. Write a script that reads in a five-digit integer
and determines whether it’s a palindrome. [Hint: Use the // and % operators to separate
the number into its digits.]'''
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
'''
3.13 (Factorials) Factorial calculations are common in probability. The factorial of a
nonnegative integer n is written n! (pronounced “n factorial”) and is defined as follows:
n! = n · (n - 1) · (n - 2) · … · 1
for values of n greater than or equal to 1, with 0! defined to be 1. So, 
5! = 5 · 4 · 3 · 2 · 1
which is 120. Factorials increase in size very rapidly. Write a script that inputs a nonnegative integer and computes and displays its factorial. Try your script on the integers 10, 20,
30 and even larger values. Did you find any integer input for which Python could not
produce an integer factorial value? '''
number=5
for i in range(1,number):
    number*=i
print(number)

"""
3.17 (Nested Loops) Write a script that displays the following triangle patterns separately, one below the other. Separate each pattern from the next by one blank line. Use for
loops to generate the patterns. Display all asterisks (*) with a single statement of the form 
print('*', end='')
which causes the asterisks to display side by side. [Hint: For the last two patterns, begin
each line with zero or more space characters.]"""
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

"""
3.18 (Challenge: Nested Looping) Modify your script from Exercise 3.17 to display all
four patterns side-by-side (as shown above) by making clever use of nested for loops. Separate each triangle from the next by three horizontal spaces. [Hint: One for loop should
control the row number. Its nested for loops should calculate from the row number the
appropriate number of asterisks and spaces for each of the four patterns.] """
# j=12
# for i in range(1,11):
#     j-=1
#     for k in range(j,0,-1):
#         print(f"{'*'*i:<10}  {'*'*k:<11}   {'*'*k:>14}  {'*'*i:>10}" )
#         break

'''Alternatively'''
# i=1
# for j in range(10,0,-1):
#         print(f"{'*'*i:<10}  {'*'*j:<10} {'*'*j:>10}  {'*'*i:>10}" ) 
#         i+=1
# 3.26 (Research: Anscombe’s Quartet) In this book’s data science case studies, we’ll emphasize the importance of “getting to know your data.” The basic descriptive statistics that
# you’ve seen in this chapter’s and the previous chapter’s Intro to Data Science sections certainly help you know more about your data. One caution, though, is that different datasets
# can have identical or nearly identical descriptive statistics and yet the data can be significantly different. For an example of this phenomenon, research Anscombe’s Quartet. You
# should find four datasets and the associated visualizations. It’s the visualizations that convince you the datasets are quite different. In an exercise in a later chapter, you’ll create
# these visualizations.'''
"""
3.20 (Binary-to-Decimal Conversion) Input an integer containing 0s and 1s (i.e., a “binary” integer) and display its decimal equivalent. The online appendix, “Number Systems,”
discusses the binary number system. [Hint: Use the modulus and division operators to pick
off the “binary” number’s digits one at a time from right to left. Just as in the decimal number system, where the rightmost digit has the positional value 1 and the next digit to the left
has the positional value 10, then 100, then 1000, etc., in the binary number system, the
rightmost digit has the positional value 1, the next digit to the left has the positional value
2, then 4, then 8, etc. Thus, the decimal number 234 can be interpreted as 2 * 100 + 3 *
10 + 4 * 1. The decimal equivalent of binary 1101 is 1 * 8 + 1 * 4 + 0 * 2 + 1 * 1."""
# number=101010
# number1=str(number)
# num_len=len(number1)
# num_space=0
# decimal_num=0
# while number>0:
#     num=number%10
#     decimal_num+=num*2**num_len
#     num_len-=1
#     number//=10

# print(f'{decimal_num}')
# '''
# 3.27 (World Population Growth) World population has grown considerably over the
# centuries. Continued growth could eventually challenge the limits of breathable air, drinkable water, arable land and other limited resources. There’s evidence that growth has been
# slowing in recent years and that world population could peak some time this century, then
# start to decline. 
# For this exercise, research world population growth issues. This is a controversial
# topic, so be sure to investigate various viewpoints. Get estimates for the current world
# population and its growth rate. Write a script that calculates world population growth
# each year for the next 100 years, using the simplifying assumption that the current growth
# rate will stay constant. Print the results in a table. The first column should display the year
#  Exercises 117
# from 1 to 100. The second column should display the anticipated world population at
# the end of that year. The third column should display the numerical increase in the world
# population that would occur that year. Using your results, determine the years in which
# the population would be double and eventually quadruple what it is today. '''

# world_population=7.9*10**9
# wp=world_population
# rate=1.05/100
# extimated_world_population=0
# double_year=0
# print(f"{'Year':<4}  {'Extimated Year':<21} {'Increase':<20}")
# for i in range(1,100):
#     world_population+=rate*world_population
#     extimated_world_population=world_population
#     ex=extimated_world_population-wp
#     if world_population>=2*wp:
#        double_year=2022+i
#        print(f'{i:<5} {world_population:<20}  {ex:<20}')
#        break
#     print(f'{i:<5} {world_population:<20}  {ex:<20} ')
    

# print(f'The year the world population doubled is {double_year}')

# '''
# 3.28 (Intro to Data Science: Mean, Median and Mode) Calculate the mean, median and
# mode of the values 9, 11, 22, 34, 17, 22, 34, 22 and 40. Suppose the values included another 34. What problem might occur?'''

# import statistics

# numbers=[9,11,22,34,17,22,34,22,40,34]
# print(statistics.mean(numbers))
# print(statistics.median(numbers))
# print(statistics.mode(numbers))
# '''The problem that occured was that it still picked 22 as the mode instead of 34'''

# '''
# 3.28 (Intro to Data Science: Mean, Median and Mode) Calculate the mean, median and
# mode of the values 9, 11, 22, 34, 17, 22, 34, 22 and 40. Suppose the values included another 34. What problem might occur? '''

# '''Answer'''
# '''You have to add the both numbers and divide them by two'''


# '''
# 3.30 (Intro to Data Science: Outliers) In statistics, outliers are values out of the ordinary
# and possibly way out of the ordinary. Sometimes, outliers are simply bad data. In the data
# science case studies, we’ll see that outliers can distort results. Which of the three measures
# of central tendency we discussed—mean, median and mode—is most affected by outliers?
# Why? Which of these measures are not affected or least affected? Why?
# '''

# """
# Answer
# The mean is most affected, for example 2,3,4,4,100, 100 is the outlier because it do not represent the distribution of the other values
# while the mode is least affected
# """


# """
# 3.31 (Intro to Data Science: Categorical Data) Mean, median and mode work well with
# numerical values. You can use them in calculations and arrange them in meaningful order.
# Categorical values are descriptive names like Boxer, Poodle, Collie, Beagle, Bulldog and
# Chihuahua. Normally, you don’t use these in calculations nor associate an order with
# them. Which if any of the descriptive statistics are appropriate for categorical data?"""

# """
# Answer
# Mode"""

"""
Write a code to display the two largest number"""

grades=[1,2,18,4,3,17,5,19,20,28]
# largestnumber=grades[0]
# secondlargestnumber=grades[0]
# for i in range(len(grades)):
#     for j in range(len(grades)):
#         if grades[j]>largestnumber:
#             largestnumber=grades[j]       
#         elif grades[j] > secondlargestnumber and grades[j] < largestnumber:
#             secondlargestnumber=grades[j]
# print(f'largest_number {largestnumber} second_largest_number {secondlargestnumber}')

#Alternatively

# largestnumber1=grades[0]
# secondlargestnumber1=grades[0]
# grades=[1,2,18,4,3,22.5,17,5,19,20,28]
# for i in range(len(grades)):
#     if grades[i]>largestnumber1:
#         secondlargestnumber1=largestnumber1
#         largestnumber1=grades[i]
# print(f'largest_number {largestnumber1} second_largest_number {secondlargestnumber1}')
        
