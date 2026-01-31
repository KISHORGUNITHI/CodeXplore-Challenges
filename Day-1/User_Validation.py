fullName=input("Enter the User Name:");
eMail=input("Enter the Email ID:");
number=input("Enter the Mobile Number:");
age=int(input("Enter the age:"));

isName=True
isEmail=True
isNumber=True
isAge=True

""" User Name validation """
if(fullName[0]==" " or fullName[len(fullName)-1]==" "):
    isName=False;
elif(fullName.count(" ")==0):
    isName=False;

""" Email ID validation """
if(not len(eMail) or " " in eMail or eMail[0]=="." or eMail[0]=="@" or "@" not in eMail or "." not in eMail):
    isEmail=False;

""" Number validation """
if(len(number)!=10 or not number.isdigit() or number[0]=="0"):
    isNumber=False;

""" Age validation """
if(age<18 or age>60):
    isAge=False;


""" Validating Data """
if(isName and isEmail and isNumber and isAge):
    print("User Profile is VALID");
else:
<<<<<<< HEAD
    print("User Profile is INVALID");
=======
    print("User Profile is INVALID");
>>>>>>> a3d269f222c1d9ad6b84ee82d0a1e4ea78a4c26d
