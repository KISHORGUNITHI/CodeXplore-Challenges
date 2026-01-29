fullName=input("Enter the User Name:");
eMail=input("Enter the Email ID:");
number=input("Enter the Mobile Number:");
age=int(input("Enter the age:"));

isName=True;
isEmail=True;
isNumber=True;
isAge=True;
""" User Name validation """
if fullName[0]==" " or fullName[len(fullName)-1]==" ":
    isName=False;
elif fullName.count(" ")==0:
    isName=False;
else:
    isName=True;

""" Email ID validation """
if(not len(eMail) or " " in eMail or eMail[0]=="." or eMail[0]=="@" or "@" not in eMail or "." not in eMail):
    isEmail=False;
else:
    isEmail=True;

""" Number validation """
if(len(number)!=10 or not number.isdigit() or number[0]=="0"):
    isNumber=False;
else:
    isNumber=True;

""" Age validation """
if(age>=18 and age<=60):
    isAge=True;
else:
    isAge=False;

""" Validating Data """
if(isName and isEmail and isNumber and isAge):
    print("User Profile is Valid");
else:
    print("User Profile is InValid");