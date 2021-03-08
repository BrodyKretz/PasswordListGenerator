import os

user_file = input("What would you like to call the password list?: ")

with open(user_file, 'w') as file:
    print("Done")

#print(os.path.exists(user_file))



#Ask

print("I will ask a series or questions about the user to better create a list to crack their password.")
print("before we start remember at anytime you want to finish with filling out information type CLEAR")
print("or you can say SKIP to skip to next prompt")


first_name = input("What is their first name?: ")
last_name = input("What is their last name?: ")
middle_name = input("What is their middle initial?: ")
birth_year = input("What is their birth year? (ex: 08): ")
birth_month = input("What is their birth month? (ex: 6): ")
birth_day = input("What is their birth day? (ex: 16): ")
pet_name = input("What is their pets name? ")

'''
so = print("That was all the important inoforamtion, if you\n would like to add more in formation(nickname, favorite color, etc.\n type y")

if so == 'y' or 'Y':
    nickname = ("What is their nickname?: ")
    favorite_color = input("What is their favorite color?: ")
    favorite_person = input("Who is their favorite person: ")
    favorite_sport = input("What is their favorite sport?: ")
    live_state = input("What state do they live in?: ")
'''
if file in['SKIP']:
    ignore

digits = ['1234567890','0123456789','0123456789']
for i in reversed(range(0,1001)):
    digits.append(str(i))


#Creates First name Passwords
first_n_list = []

first_n_list = [first_name + d for d in digits]
first_n_list.append(first_name + birth_year)
first_n_list.append(first_name + birth_month + birth_day)
first_n_list.append(first_name + birth_year + birth_month + birth_day)
#change
first_name_n = first_name + last_name[0]
#repeat above
first_ne_list = [first_name_n + d for d in digits] #trying to grab value and use next one after
first_n_list.append(first_name_n + birth_year)
first_n_list.append(first_name_n + birth_month + birth_day)
first_n_list.append(first_name_n + birth_year + birth_month + birth_day)


#Creates Last name Passwords
last_n_list = []
last_n_list = [last_name + d for d in digits]
last_n_list.append(last_name + birth_year)
last_n_list.append(last_name + birth_month + birth_day)
last_n_list.append(last_name + birth_year + birth_month + birth_day)

#First letter of last name
last_name_n = first_name[0] + last_name

last_n_list = [last_name_n + d for d in digits]
last_n_list.append(last_name_n + birth_year)
last_n_list.append(last_name_n + birth_month + birth_day)
last_n_list.append(last_name_n + birth_year + birth_month + birth_day)


#Creates Middle name Passwords
middle_name_list = []

full_name = first_name + middle_name + last_name

middle_name_list.append(full_name)
middle_name_list = [full_name+ d for d in digits]
middle_name_list.append(full_name + birth_year)
middle_name_list.append(full_name + birth_month + birth_day)
middle_name_list.append(full_name + birth_year + birth_month + birth_day)

#Creates pet Passwords
pet_name_list = []

pet_name_list.append(pet_name + 'iscute')
pet_name_list.append('ilove' + pet_name)
pet_name_list.append(pet_name + 'love')
pet_name_list.append(pet_name + '101')
pet_name_list.append(pet_name + '123')
pet_name_list = [pet_name + d for d in digits]
file_text = middle_name_list + last_n_list + first_n_list + pet_name_list + first_ne_list

with open(user_file, 'w')as f:
    for pw in file_text:
        f.write(pw + '\n')

