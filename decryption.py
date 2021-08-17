#!/bin/python3
import os

def encrypt():
    os.system("ls")
    file = input("""

------------------------------------------------------------
type entire file + extension, that you would like to encrypt
------------------------------------------------------------

""")
    os.system("clear")
    os.system("gpg -c " + file)
    os.system("rm " + file)
    print("""

---------------------------------------
The file has been encrypted
---------------------------------------

""")
    MAIN_loop()

def decrypt():
    os.system("ls")
    file = input("""

------------------------------------------------------------
type entire file + extension, that you would like to decrypt
------------------------------------------------------------

""")
    os.system("clear")
    os.system("gpg -d " + file)
    print("""

---------------------------------------
The file has been decrypted
---------------------------------------

""")
    MAIN_loop()

def permanentdecrypt():
    os.system("ls")
    file = input("""

------------------------------------------------------------
type entire file + extension, that you would like to decrypt
------------------------------------------------------------
""")
    newfile = input("""

----------------------------------
rename decrypted file + extension
----------------------------------
""")
    os.system("sudo touch " + newfile + " ; sudo chmod 555 " + newfile + " ; gpg -d " + file + "| cat > " + newfile)
    print("""

---------------------------------------
The file has been decrypted
---------------------------------------

""")
    if os.popen('whoami').read() == "root":
        os.system("rm " + file)
    MAIN_loop()

def MAIN_loop():
    while True:
        choice = input("""

-------------------------------------------

would you like to encrypt or decrypt a file

TYPE 'e' for encrypt or 'd' for decrypt

to EXIT type 'done'

-------------------------------------------

""")
        choice = choice.lower()
        if choice == "e" or choice == "encrypt":
            encrypt()
        elif choice == "d" or choice == "decrypt":
            option = input("""

------------------------------------------------
would you like to perminantly decrypt the file?

y for yes, n for no

-Side Note-
if yes, must be root or it will delete all info
inside file, leave this program and sign in as
root.
------------------------------------------------

""")
            option = option.lower()
            if option == "y" or option == "yes":
                permanentdecrypt()
            elif option == "n" or option == "no":
                decrypt()
        elif choice == "done":
            exit()
        else:
            print("Error; could not locate 'e' or 'd', please try again")


MAIN_loop()

