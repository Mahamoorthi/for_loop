x=int(input("enter the number:"))
temp=x
rev=0
while(x>0):
    dig=x%10
    rev=rev*10+dig
    x=x//10
if(temp==rev):
    print("the number is palindrome")
else:
    print("the number is not palindrome")

