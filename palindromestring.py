def palindrom():
    stri=input("enter the string  ")
    s=""
    for i in stri:
        s=i+s
    if(stri==s):
        print("its a palindrom string ")
    else:
        print("its not a palindrom string")
palindrom()
