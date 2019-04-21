#random password generator
import random
import string

def encrypt(pass_length, fileName):
    global rando
    global i
    global pass_temp
    global password
    global ascii_range
    
    rando = ''
    password = ""
    i = 0
    while i < pass_length:
        print(rando)
        rando = chr(random.randint(41,126))
        password += rando
        i += 1
    #CREATE .txt file that has the password
    print("Your password:", password)

    pass_file = open(fileName + ".txt","w+")

    pass_file.write("Here's your password: " + password)

    pass_file.close()




