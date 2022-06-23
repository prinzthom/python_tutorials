"""
Insert your username : prince
Insert your email : prince@thomas.com
Insert your password : prince123
Welcome to the System!
OR
Invalid Credentials
"""

usrnme_in = input("insrt your username: ")
eml_in= input("insert your email: ")
pssd_in= input("insert your password: ")

if usrnme_in == "prince" and eml_in == "prince@thomas.com" and pssd_in == "prince123":
    print ("Welcome to the system")
else :
    print("invalid credentials!")
