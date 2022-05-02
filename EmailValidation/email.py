# Python code for check Validate E-Mail Address 

email = input("Enter your email : ")  # take input from the user
k, j, d = 0, 0, 0
if len(email) >= 8:
    if email[0].isalpha(): # check first character is alphabet
        if ("@" in email) and (email.count("@") ==1): # @ should not use more than one times
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace(): # check under score in email
                        k = 1
                    elif i.isalpha():
                        if i == i.upper(): # check uppercase in email
                            j = 1
                    elif i.isdigit(): # check number in email
                        continue
                    elif i =="_" or i=="." or i =="@":
                        continue
                    else:
                        d = 1
                if k ==1 or j ==1 or d==1:
                    print("Wrong Email 5")
                else:
                    print("Right Email")
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")