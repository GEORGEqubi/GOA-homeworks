

n = int(input("Enter Number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i
print(factorial)

# % ოპერატორი აბრუნებს ნაშთს, რომელიც რჩება ერთი რიცხვის მეორეზე გაყოფის შემდეგ.


num = int(input("Enter Number: "))

for i in range(1, num + 1):
    if num % i == 0:
        print(i)