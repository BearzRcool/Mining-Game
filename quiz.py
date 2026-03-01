'''
1   Declare a variable and assign it to an integer, then output the number raised to the power of 3.	10pts	
2	Declare a variable and assign it to the list [1,2,3,4,5]. Calculate then output the sum of the list.	20pts	
3	Print the numbers from 1 to 100 and skip anything that is divisible by 9.	20pts	
4	Declare a variable and assign it to ”Programming isn't about what you know; it's about what you can figure out.” then calculate the count of the number of words in the variable and output the number.	30pts	
5	Declare a variable and assign it to any number, and output the last digit of the number. Input 2345 would output 5, while 9876 would output 6.	30pts	
6	Declare a variable and assign it to a string value. Then output the string where each letter in the word must be one of these characters: 't', 'u', 'r', 'i', 'n', 'g'. Otherwise omit that letter. An example would be: 'fun rigid' would output: 'unrigi'.	30pts	
7	Declare a variable and assign it to the list [1,2,3,4,5]. Calculate then output the list in reverse order. We will be changing the values when grading.	40pts	
8	Declare a variable and assign it to a string ”seven”. Output the string with 1 of the first letter followed by 2 of the second letter followed by 3 of the third letter and so on. We will be changing the values when grading.	40pts	
9	Declare a variable and assign it to a positive integer. Take the remainder of the number divided by 7, assume 0 is ”Sunday”, and 6 is ”Saturday”, and the other days in string form correspond to numbers accordingly. Output which day of the week it is. We will be changing the values when grading.	50pts	
10	Declare a variable and assign it to ”froglizardfroglizard”. Output True if ”frog” and ”lizard” appear the same amount of times. Output False if different. We will be changing the values when grading.	50pts	
11	Declare a variable and assign it to the list[8,6,2,8,7,5,2]. Return the sum of the numbers in the list, except leave out any 8's or 2's. The example would return the answer 18. We will be changing the values when grading.	50pts	
12	Declare two variables, list1 and list2, and assign them to [1,2,3] and [4,5,6]. Convert them into a dictionary named dict1 in a way that item from list1 is the key and item from list2 is the value.	60pts	
13	Declare two variables assigned to two positive integers, then output the greatest common divisor of the two numbers. (105,45) would output 15, while (36, 42) would output 6.	70pts	
14	Declare an integer called debitcard and assign it to 4253665879515786. Output ”valid” if the values are valid. Use these rules to determine if the debit card number is valid.
1. It must start with a 4, 5, or 6.
2. It must contain exactly 16 digits.
3. It can not have 4 or more consecutive repeated digits.
NOTE: We will be changing the values when grading.
80pts	
15	Declare a string and assign it to ”135246ABCzyx”. Output the sorted version of the string using these rules.
1. Sorted uppercase letters are ahead of lowercase letters.
2. Sorted lowercase letters are ahead of digits.
3. Sorted odd digits are ahead of sorted even digits.
NOTE: We will be changing the values when grading.
80pts	
16	Declare a list and assign it to [”Everywhen”, ”Erf”, ”Bumbershoot”, ”Cleek”, ”Finifugal”]. Output the score of the list based on the rule that each string has a value of 2 if the number of vowels in the string is odd, 1 otherwise. The answer of the current list is 7. We will be changing the values when grading.	90pts	
17	Implement bubble sort and call it on a list of 10 numbers, sorting from smallest to largest. Output the sorted list. You cannot use a library for this solution.	100pts'''
import random
num1 = 5
power = 5**3
#print(power)


num2 = [1,2,3,4,5]
def SumofList(nums):
    total = 0
    for num in nums:
        total+=num
    return total

def SkipNine():
    for i in range(1,101):
        if i %9 != 0:
            print(i)

num4 = "Programming isn't about what you know; it's about what you can figure out."
def WordCount(string):
    words = 0
    isFirst = True
    for i in range(len(string)):
        if string[i] == ' ':
            if isFirst:
                if string[i-1] != ' ':
                    words += 1
                isFirst = False
            if string[i+1] != ' ':
                words += 1
    print(words)

num5 = 12345
def LastNum(number):
    number = str(number)
    print(number[len(number)-1])
#LastNum(num5)
chars = ['t', 'u', 'r', 'i', 'n', 'g']
words = 'loading'
num6 = ''
for word in words:
    for letter in chars:
        if word == letter:
            num6 += letter
#print(num6)

num7 = [1,2,3,4,5]
def reverse(numbers):
    reverse = []
    for i in range(len(numbers),0,-1):
        reverse.append(i)
    print(reverse)
#reverse(num7)
seven = 'seven'
def number8(string):
    times = 1
    new_word = ""
    for i in string:
        new_word += i*times
        times += 1
    print(new_word)
#number8(seven)
num9 = random.randint(1,8)

week = {0: 'sunday', 1: 'Monday', 2:"Tuesday",3:"Wednesday",4:"Thursday",5:'Friday',6:'Saturday'}
def modulo7(number,week):
    print(number)
    check = number%7
    print(week.get(check))
#modulo7(num9,week)
def froglizard(string):
    string = string.lower()
    TotalF = 0
    TotalL = 0
    for i in string:
        if i == 'f':
            TotalF += 1
        elif i == 'l':
            TotalL += 1
    if TotalF == TotalL:
        return True
    return False
num10 = 'froglizardfrog'
#print(froglizard(num10))

num11 = [8,6,2,8,7,5,2]
def noEightorTwo(numbers):
    total = 0
    for i in numbers:
        if i != 8 and i != 2:
            total += i

    print(total)
#noEightorTwo(num11)
list1 = [1,2,3]
list2 = [3,4,5]
def DictMaker(list1, list2):
    my_dict = {}
    for i in range(len(list1)):
        my_dict[list1[i]] = list2[i]
    print(my_dict)
#DictMaker(list1,list2)
var1 = 105
var2 = 45
def GCF(number1, number2):
    check = 0
    if number1 > number2:
        check = number2
    elif number2 > number1:
        check = number1
    else:
        return number1
    for i in range(check,1,-1):
        if number2%i == 0 and number1%i == 0:
            return i

#print(GCF(var1,var2))  
credit_card = 4253665879515786
def checkCreditCard(num):
    num = str(num)
    if len(num) != 16:
        print('length wrong')
        return 'Not Valid'
    
    elif num[0] != '4' and num[0] != '5' and num[0] != '6':
        return "Not Valid"
    
    for i in range(len(num)):
        quad = num[i:i+4]
        try:
            if quad[0] == quad[1] == quad[2] == quad[3]:
                return 'Not Valid'
        except:
            pass
    return "Valid"
#print(checkCreditCard(credit_card))
words = ['Everywhen', 'Erf', 'Bumbershoot', 'Cleek', 'Finifugal']
def Vowels(words):
    answer = 0
    for word in words:
        
        vowels = 0
        for letter in word:
            letter = letter.lower()
            
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
                
                vowels += 1
        if vowels%2 == 0:
            answer += 1
        else:
            answer += 2
        
    print(answer)
#Vowels(words)
ten_nums = [1,6,2,3,5,4,7,9,8,10]
def FindMax(list):
    biggest = 0
    pos = 0
    for i in range(len(list)):
        if list[i] > biggest:
            biggest = list[i]
            pos = i

    return pos
def Bubble_sort(nums):
    
    repeats = 0
    for i in range(len(nums)):
        biggest = FindMax(nums[::len(nums)-repeats])
        for number in range(biggest,len(nums)-repeats-1):
            if nums[number+1] < nums[number]:
                placeholder = nums[number+1]
                nums[number+1] = nums[number]
                nums[number] = placeholder
        repeats += 1
    print(nums)

#Bubble_sort(ten_nums)
'''
finds biggest num, then moves to the last position in the list
finds the second biggest num, then moves to second last in the list
repeat until least to greatest
did ^ without python libraries
'''



radix_nums = [222,33,1]
def Radix_sort(nums):
    max_value = max(nums)
    max_value_digits = str(max_value)
    for i in range(len(max_value_digits)):
        pass
Radix_sort(radix_nums)