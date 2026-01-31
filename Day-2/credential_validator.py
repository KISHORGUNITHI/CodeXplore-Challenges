isId=False
isEmail=False
isPass=False
isCode=False
studentID = input("Enter Student ID: ");
emailID = input("Enter Email ID: ");
password=input("Enter Password: ");
referral_code=input("Enter Referral Code: ");

""" Student ID validation """
start=studentID[0]+studentID[1]+studentID[2]+studentID[3];
if(len(studentID)==7 and 
        start=="CSE-" and 
        studentID[4].isdigit() and 
        studentID[5].isdigit() and 
        studentID[6].isdigit()):
    isId=True

""" Email ID validation """
if(emailID.endswith("@univ.edu")
        and'a'<=emailID[0].lower()<='z'
        and emailID.count("@")==1
        and emailID.count(".")==1
        and emailID.find(" ")==-1):
    isEmail=True

""" Password validation """
if(len(password)>=8
    and 'A'<= password[0] <='Z'
    and ('0' in password or '1' in password or
        '2' in password or '3' in password or
        '4' in password or '5' in password or
        '6' in password or '7' in password or
        '8' in password or '9' in password)):
    isPass=True

""" Referal Code validation """
if(len(referral_code)==6
        and referral_code.startswith("REF")
        and referral_code[3].isdigit() and referral_code[4].isdigit()
        and referral_code[len(referral_code)-1]=="@" ):
    isCode=True

if(isId and isEmail and isPass and isCode):
    print("APPROVED")
else:
    print("REJECTED")