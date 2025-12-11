# 2) დაბეჭდეთ რიცხვები 10-დან -10ის ჩათვლით

for i in range(10, -11, -1):
    print(i)

# 3) დაბეჭდეთ ყველა კენტი რიცხვი 1-დან 100-ის ჩათვლით

for i in range(1, 100, 2):
    print(i)

# 4) მომხმარებელს შემოატანინეთ პაროლი იქამდე სანამ ის არ გაუტოლდება "goa123"-ს, ამასთან ერთად მას უნდა ჰქონდეს მხოლოდ
#  3 მცდელობა სწორი პაროლის შესაყვანად. ყოველი არასწორი მცდელობისას დაუბეჭეთ "Password is incorrect! Try again", ასევე დაუბეჭდეთ ის თუ რამდენი მცდელობა(მხოლოდ რიცხვი არა, ტექსტი გასაგებად).

password = "goa123"
print("you have 3 tries")
userpassword =input("Enter password: ")
tries = 2
while userpassword!=password and tries > 0:
    print("Password is incorrect! Try again")
    print("You have " + str(tries) + " tries left")
    userpassword =input("Enter password: ")
    tries -= 1
    


