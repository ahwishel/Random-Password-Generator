#random password generator
import random
import string
import optparse

def encrypt(pass_length, fileName):
    rando = ''
    password = ""
    i = 0
    while i < int(pass_length):
        rando = chr(random.randint(41,126))
        password += rando
        i += 1
    #CREATE .txt file that has the password
    print("Your password:", password)

    pass_file = open(fileName + ".txt","w+")

    pass_file.write("Here's your password: " + password)

    pass_file.close()

if __name__ == '__main__':
    parser = optparse.OptionParser(f'usage %prog -l <password length> -f <filename>')
    parser.add_option('-l', dest='passLength', type='int', help='Please enter password length after -l flag')
    parser.add_option('-f', dest='filename', type='string', help='Please enter path + filename where you want to save your password after the -f flag')
    (options, args) = parser.parse_args()
    encrypt(options.passLength, options.filename)




