num=int(input("Enter a number to be reversed:"))
int sum=0
temp=num
while(num!=0):
    rem=num%10
    sum=sum+rem*rem*rem
    num=num/10
if(sum==temp):
    print("The number is armstrong")
else:
    print("the number is not an armstrong")
