
# შედარების ოპერატორები: >, <, >=, <=, ==, !=

3 > 1
22 > 13
123 > 45
65 > 31
33 > 27

3 < 44
44 < 55
123 < 376
54 < 57
22 < 99

43 >= 43
14 >= 4
88 >= 53
64 >= 64
42 >= 11

23 <= 23
63 <= 94
44 <= 51
14 <= 14
1 <= 0
 
1 == 1
13 == 13
11 == 99
33 == 13
14 == 14

5!=5
11!=14
44!=44
134!=999
431!=31

# logical operators- and, or  გამოიყენება შედარების შედეგების გასაერთიანებლად
# and ოპერატორი აბრუნებს True-ს მხოლოდ მაშინ თუ შედარებაში ყველა პირობა არის-True
# or ოპერატორი აბრუნებს True-ს იმ შემთხვევაში თუ მხოლოდ 1 პირობა მაინც არის True


# and
num1= 33==11
num2= 6<=56    

print(num1 and num2)  #False

num1= 11>4
num2= 99>53

print(num1 and num2) #True

num1= 53==11
num2= 13!=13

print(num1 and num2) #False

# or
num1= 33>=14
num2= 11<=124

print(num1 or num2) #True

num1= 114<999
num2= 13>14

print(num1 or num2) #True

num1= 12>=55
num2= 153>=999

print(num1 or num2) #False




number= 34

number1= int(input("Please Enter Any Number: " ))

result= number<number1

print(result)



age = 18
User_Age = int(input("Please enter your age: "))

result1= User_Age>age

print(result1)

My_name = "George"

User_name = input("Enter your name: ")

print(My_name == User_name)
















