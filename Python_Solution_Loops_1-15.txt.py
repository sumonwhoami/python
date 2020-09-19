#1. Write a python program to find the sum of first 10 natural numbers.
#solution:
# n = 10
# sum = 0
# for i in range(n):
#     sum = sum + i
# print(sum)

#2. Write a program in python to display n terms of natural number and their sum.
# n = int(input("Type n terms of natural number: "))
# sum = 0
# for i in range(n):
#     sum = sum + i
# print("The sum of n terms: ", sum)    

#3-4. Write a program in python to input 10 numbers from keyboard and find their sum and average. 
# n = 10
# sum = 0
# for i in range(n):
#     numberlist = float(input("Enter your numbers : "))
#     sum = sum + numberlist
#     avg = sum / n
# print("The sum is: ",sum,"and", "The avg is: ", avg)

#5. Write a program in python to display the n terms of odd natural number and their sum.
# n = int(input("Your natural number : "))
# sum = 0

# for i in range(n):
#     if (i % 2 != 0):
#         print("the odd numbers: ", i)
#         sum = sum + i
# print("The Odd Sum: ", sum)    

#6. Write a program in python to display the n terms of square natural number and their sum. 1 4 9 16 ... n Terms
# n = int(input("Enter your natural number: "))
# sum = 0

# for i in range(1,n+1):
#     squareofn = i**2
#     print("The square numbers: ", squareofn)
#     sum = sum + squareofn
# print("\nThe sum of square numbers: ", sum)    

#7. Write a program in python to find the number and sum of all integer between 100 and 200 which are divisible by 9.
# n1 = 100
# n2 = 200
# sum = 0

# for i in range(n1,n2+1):
#     if i%9 == 0:
#         print("the numbers: ", i)
#         sum = sum + i
# print("The sum of 9 divisible numbers is: ", sum)        

#8. Write a program in python to count total number of alphabets, digits and special characters in a string.
# thestring = "aeiou 747 #$%! bcvftxyz"
# alphabets = digits = specialchar = 0

# for i in range(len(thestring)):
#     if(thestring[i].isalpha()):
#         alphabets = alphabets + 1
#     elif(thestring[i].isdigit()):
#         digits = digits + 1
#     else:
#         specialchar = specialchar + 1    

# print("\nTotal Number of Alphabets in this string is : ", alphabets)
# print("\nTotal Number of Digits in this string is : ", digits)
# print("\nTotal Number of Special Character in this string is : ", specialchar)

#9. Write a program in python to count total number of vowel or consonant in a string.
#thestring = "aeIOu sdbxyz 123ceo"
# thestring = input("type your input from user here : ")
# vowels = consonants = others = 0

# for i in thestring:
#     if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
#        or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
#        vowels = vowels + 1
#     elif(i == 'b' or i == 'c' or i == 'd' or i == 'f' or i == 'g' or i == 'h' or i == 'j' or i == 'k' or i == 'l' 
#     or i == 'm' or i == 'n' or i == 'p' or i == 'q' or i == 'r' or i == 's' or i == 't' or i == 'v' or i == 'w' or i == 'x' or i == 'y' or i == 'z'
#     or i == 'B' or i == 'C' or i == 'D' or i == 'F' or i == 'G' or i == 'H' or i == 'J' or i == 'K' or i == 'L' or i == 'M' or i == 'N' or i == 'P' 
#     or i == 'Q' or i == 'R' or i == 'S' or i == 'T' or i == 'V' or i == 'W' or i == 'X' or i == 'Y' or i == 'Z' ):
#         consonants = consonants + 1   
#     else:
#         others = others + 1
# print("\nTotal Number of Vowels in the String = ", vowels)
# print("\nTotal Number of Consonants in the String = ", consonants)
# print("\nTotal Number of others in the String = ", others)

#10. Write program in python to check a list is empty or not.
# thelist = input("type anything to check thelist is EMPTY or NOT : ")
# if len(thelist) == 0:
#     print("thelist is empty !")
# else:
#     print("thelist is NOT empty!")    

#11. Write a program in python to sum all the items in a list. 
# thelist = [5, 10, 15, 5]
# sum = 0

# for i in range(len(thelist)):
#     sum = sum + thelist[i] 
# print("the sum :", sum)

#12. Write a program in python to get the largest number from a list.
# thelist = [5, 7, 9, 2, 3, 15, 13, 10]
# print("The largest number in thelist : ", max(thelist))

# thelist = [5, 7, 9, 2, 3, 15, 13, 10]
# print("The minimum number in thelist : ", min(thelist))

#13. Write a program in python to print the numbers of a specified list after removing even numbers from it.
# thelist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in thelist:
#     if i%2 != 0:
#         print("The odd numbers : ", i) 

#14. Write a program in python to convert a list of characters into a string.
# listofchar = ['b', 'a', 'n', 'g', 'l', 'a', '1', '9', '7', '1']
# convtostring = ''.join(listofchar)
# print(convtostring)

#15. Write a program in python to convert a list of multiple integers into a single integer. 
#    Sample list: [2, 54, 6, 1000]
#    Expected Output: 25461000
# samplelist = [2, 54, 6, 1000]
# for i in samplelist:
#     print(i,end='')
