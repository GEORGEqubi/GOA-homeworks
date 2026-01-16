# 2) გაიმეორეთ ნასწავლი მასალა: for loop, while loop, if/elif/else
#  და მათი კომბინაციით გააკეთეთ რამოდენიმე მარტივი მაგალითი.



for i in range (1, 11): # 1 დან 10 ის ჩათვლის ყველა ლუწი რიცხვი.
    if i % 2 == 0:
        print(i)

for i in range (1, 11): # ამოწმებს რიცვებს 1 - დან 10-ამდე კენტია თუ ლუწი.
    if i % 2 == 0:
        print(i, "ლუწია")
    else:
        print(i, "კენტია")

i = 1
while i <= 10: # ვბეჭდავთ რიცხევბს 1 -დან 10-ის ჩათვლით while loop - ის გამოყენებით.
    print(i)
    i += 1

# თამაში გამოიცანი ჩემი სახელი.
trys=2
my_name = "George"
guesed_name = input("guess the name. you have 3 tries: ")
while guesed_name != my_name and trys > 0:
    print("name is incorrect, try again")
    print("you have " + str(trys) + " left")
    guesed_name = input("guess the name. you have 3 tries: ")
    trys -= 1
    if guesed_name == my_name:
        print("name is correct you win!")
