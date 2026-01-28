
# 2) STRING-ის ფუნქციები 


# .upper()
# გადააქცევს string-ში ყველა ასოს დიდ ასოდ

text = "gamarjoba"
print(text.upper())         

text2 = "Python"
print(text2.upper())         

text3 = "hello world"
print(text3.upper())         


# .lower()
# გადააქცევს string-ში ყველა ასოს პატარა ასოდ

text = "GAMARJOBA"
print(text.lower())          

text2 = "PyThOn"
print(text2.lower())         

text3 = "HELLO WORLD"
print(text3.lower())         


# .capitalize()
# პირველ ასოს აქცევს დიდად, დანარჩენებს პატარად

text = "gamarjoba"
print(text.capitalize())   

text2 = "PYTHON"
print(text2.capitalize())    

text3 = "hELLO"
print(text3.capitalize())    

# .title()
# თითოეული სიტყვის პირველ ასოს აქცევს დიდად

text = "hello world"
print(text.title())          

text2 = "python programming language"
print(text2.title())        

text3 = "my name is giorgi"
print(text3.title())         


# .find()
# ეძებს სიმბოლოს ან სიტყვას string-ში
# აბრუნებს ინდექსს (თუ ვერ იპოვა, აბრუნებს -1)

text = "hello world"
print(text.find("w"))       

text2 = "python"
print(text2.find("o"))      

text3 = "gamarjoba"
print(text3.find("z"))      




# 3) DOT NOTATION

# Dot notation ნიშნავს წერტილის (.) გამოყენებით
# ობიექტის ფუნქციების  გამოძახებას

# string არის ობიექტი და მას აქვს თავისი ფუნქციები
text = "hello"

# აქ .upper() არის string-ის მეთოდი,
# რომელსაც ვიძახებთ dot notation-ის მეშვეობით
print(text.upper())          


print(text.lower())          
print(text.capitalize())     
print(text.find("e"))        


