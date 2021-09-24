
address_book = {"Name" : [], "Surname" : [], "Email" : [], "Phone" : []}
print(address_book)
name = []
surname = []
email = []
phone = []
step = 5
while step > 0:
    a = input("Please enter name:")
    b = input("Please enter surname:")
    c = input("Please enter email:")
    d = input("Please enter phone:")
    name.append(a)
    surname.append(b)
    email.append(c)
    phone.append(d)
    step = step - 1
print(name,surname,email,phone)


 