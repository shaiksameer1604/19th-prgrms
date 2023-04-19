num=int(input("Enter a number to be reversed:"))
int rev,rem=0,0
while(num!=0):
    rem=num%10
    rev=rev*10+rem
    num=num/10
print("Reversed number is {}".format(num))    