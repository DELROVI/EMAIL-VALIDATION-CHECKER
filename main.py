email=input("Enter your Email")#helloabc@gmail.com
k,j,d=0,0,0
if "@" in email:
    username,domain=email.split("@")
if len(username)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if(email[-3]=="." or email[-4]=="."):
                for i in email:
                    if i.isspace():
                        k=1
                    elif i.isalpha():
                        if i.isupper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k ==1 or j==1 or d==1:
                    print("INVALID SYNTAX USED")
                else:
                    print("The Email is Valid")
            else:
                print("YOU CANNOT LEAVE THE DOT AT LAST!!!")
        else:
            print("Email is invalid 'EMAIL MUST CONTAIN AT MOST ONE @'")
    else:
        print("Email is invalid 'EMAIL MUST BEGIN WITH ALPHABET'")
else:
    print("Email is invalid 'USERNAME MUST AT LEAST BE OF 6 CHARACTERS'")