#  კომენტარებთ ახსენით რა არის type ფუნქცია და გააკეთეთ თითო მაგალითი ყველა ნასწავლ მონაცმეთა ტიპზე

# type()- ფუნქცია რომელიც ამოწმებს მისთვის გადაცემული მონაცემის ტიპს 

# 3) კომენტარებით ახსენით რა არის Data convertion, ჩამოწერეთ მასთან დაკავშირებული დღეს ნასწავლი ფუნქციები, 
# ახსენით თითოული მათგანი კომენტარით და თითოზე გააკეთეთ 3-3 მაგალითი

# Data convertion- მონაცემის ერთი ტიპიდან მეორეზე გარდაქმნა

# int() გარდაქმნის მნიშვნელობას მთელ რიცხვად
# float() გარდაქმნის მნიშვნელობას წილად რიცხვად
# str() გარდაქმნის მნიშვნელობას ტექსტად
# bool() გარდაქმნის მნიშვნელობას  (True/False)

# int()
a = int("334")
b = int(3.4)
c = int(True)

# float()
a1 = float("123")
b1 = float(651)
c1 = float(False)

# str()
a2 = str(12)
b2 = str(2.4)
c2 = str(False)

# bool()
a3 = bool(0)
b3 = bool("python")
c3 = bool(3.4)


# მომხმარებელს შემოატანინეთ 3
#  რიცხვი, ჯერ დაბეჭდეთ მათი ჯამი, შემდეგ კი გადაიყვანეთ თითოეული 
# მათგანი string მონაცემთა ტიპად, მოახდინეთ მათ შორის კონკადინაცია
# და დაბეჭდეთ

num1 = int(input("Please enter the number: "))
num2 = int(input("Please enter the number: "))
num3 = int(input("Please enter the number: "))

print(num1+num2+num3)

str1=str(num1)
str2=str(num2)
str3=str(num3)

print(str1+str2+str3)

# მომხმარებელს შემოატანინეთ მისი სახელი, შემდეგ კი ნებისმიერი მთელი რიცხვი.
#  დაბეჭდეთ შემოტანილი სახელი იმდენჯერ, რა რიცხვიც შემოიტანა მომხმარებელმა

user_name = input("Please enter your name: " )
any_int = int(input("Choose any integer: "))

print(user_name * any_int)

