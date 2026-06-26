import random
import string

print("====Random passowrd Generator====")
length=int(input("enter password length here: "))
Rp = string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(length):
    password+=random.choice(Rp)
print(password)