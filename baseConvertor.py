"""
Name:Christina He
UCID: 30168171
Instructor: Jonathan Hudson
TA: James Chow
Course: summer 2021 duel credit cpsc217
Assignment 1 part 2

How this program works?
Every base can be expressed in the form of decimal through:
a * x ^ 0 + b * x ^1 + c * x ^ 2 ...  x = base (ex. base2)

Therefore, in order to find the decimal, we only need to use the digits
of the base times base to the power of digits(Note: the digit here start with 0)

In order to convert decimal to base, is more complicated than converting base
to decimal. However, there is a universal method called division algorithm to help us out.

Bases are expressed as cba[base].
Since we only need to find cba, we can get rid of x ^ 2, x ^ 1, x ^ 0.
To do that, we can first use modulo to determine the remainder of the decimal.
(a * x ^ 0 + b * x ^1 + c * x ^ 2) % x
This leaves the remainder a * x ^ 0,
since x ^ 0 = 1, the remainder = a.

Then get rid of the remainder through integer division //.
(a * x ^ 0 + b * x ^1 + c * x ^ 2) // base = (b * x ^0 + c * x ^ 1)

Notice b * x ^ 1 is reduced to x ^ 0?
We can repeat the process used on a until all exponent is reduced to 0.
In this case we get a, b, and c in the form of remainder.
By reversing the remainders abc -> cba, we get our final answer in base.

(Note: In base, when numbers are getting larger than 9, we use letters from a-z
to present instead.)
(Note: Since I'm putting in the numbers myself, therefore I omitted the exception
part.)
"""
# This list is used later for question 7 to store the decimals when converting the base to base 10
valueForQ7 = []
questionDefault = 0

# define a general function to convert decimal to base.
# taking base number and decimal number as arguments.
def toBase(baseNum,dec):
    # initiate variables, base here is the representation of decimal in base.
        base = ""
        temp = dec
    # loop until all exponent reduced to 0 (X ^ 0 // anything greater than one = 0)
        while temp != 0:
            # Use letters to represent integers greater than 9 (change only to capital letters)
            if temp % baseNum < 10:
                base = base + str(temp % baseNum)
            else:
                base = base + chr((temp % baseNum)+55)
            # integer division
            temp = temp // baseNum
        # reverse the string
        base = base[::-1]
        # format and output the result
        print("decimal:{0} answer:{1}[{2}]".format(dec,base,baseNum))


# Define a general function for converting base to decimal
# base refers to the number in base(ex. 96C), baseNum is the base number(ex. hexadecimal is 16)
# question is used to identify which question this applies to.
# I'm taking in the results for question 7 to be used as the value in toBase function.
def fromBase(base,baseNum,question=questionDefault):
    decimal = 0
    # convert base into a list of strings
    temp = ",".join((base.upper())[::1]).split(",")
    if baseNum > 10:
        # The code about list comprehension is derived from
        # www.geeksforgeeks.org/python-replace-substring-in-list-of-strings/amp/
        # It replaces a specific letter in substring in the list
        # Since the highest base needed to convert to decimal in the assignment is base 16, I only coded to f.
        temp = [sub.replace('A','10') for sub in temp]
        temp = [sub.replace('B','11') for sub in temp]
        temp = [sub.replace('C','12') for sub in temp]
        temp = [sub.replace('D','13') for sub in temp]
        temp = [sub.replace('E','14') for sub in temp]
        temp = [sub.replace('F','15') for sub in temp]

    # Converting bases to decimal
    for count in range(len(temp)):
        temp[count] = int(temp[count])
        decimal += (temp[count]) * baseNum ** (len(temp)-count-1)
        # check if it is question 7, if true, adding the result to the list.
    if question == 7:
        valueForQ7.append(decimal)
        # format and output the result
    print("base:{0}[{1}] decimal:{2}[10]".format(base,baseNum,decimal))

# conversions
# Calling the functions and apply it to each item in the list
# 1-4
print("Question 1-4")
numbers = [768,562,4636,2746,869263]

for number in numbers:
    toBase(2,number)
    toBase(5,number)
    toBase(8,number)
    toBase(16,number)

# 5
print("Question 5")
numbers = ["101","11001","1100110","101011000","1011110101000100110"]
for number in numbers:
    fromBase(number,2)

#6
print("Question 6")
fromBase("2301",5)
fromBase("2451",6)
fromBase("1a3",16)
fromBase("150",8)
fromBase("8261",9)

#7
print("Question 7")

fromBase("F1",16,7)
fromBase("10101110100",2,7)
fromBase("DAB",15,7)
fromBase("3241",6,7)
toBase(7,valueForQ7[0])
toBase(4,valueForQ7[1])
toBase(20,valueForQ7[2])
toBase(16,valueForQ7[3])
