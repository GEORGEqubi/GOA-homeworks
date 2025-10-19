#  კომენტარებით ახსენით რა არის input/output-ი და მოიყვანეთ მათი მაგალითები.

#  input-არის პროცესი როდესაც კომპიუტერში შედის ინფორმაცია. მაგალითად-კლავიატურაზე წერისას, მიკროფონში ლაპარაკისას.
#  output-არის პროცესი როდესაც კომპიუტერიდან ვიღებთ რაიმე ინორმაციას. მაგ-მონიტორზე გამოსული გამოსახულება, დინამიკებიდან გამოსული ხმა.


# მომხმარებელს შემოატანინეთ ორი სიტყვა, შეინახეთ ისინი ცვლადში, მოახდინეთ მათი კონკადინაცია და დაბეჭდეთ


name = input("What is your name?: ")
surname = input("What is your lastname: ")

print("hello " + name + surname)

# მომხმარებელს შემოატანინეთ 5 რიცხვი და დაბეჭდეთ მათი საშუალო არითმეტიკული(დაგჭირდებათ int ფუნქცია).

num1 =int(input("choose any number one to ten: "))
num2 =int(input("choose any number one to ten: "))
num3 =int(input("choose any number one to ten: "))
num4 =int(input("choose any number one to ten: "))
num5 =int(input("choose any number one to ten: "))


print (float((num1 + num2 + num3 + num4 +num5) / 2))


