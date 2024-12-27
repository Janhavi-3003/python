n=int(input())
rev=0
while n!=0:#567|56|5|0 it will exits the loop
    rem=n%10#for last digit 7|6|5
    rev=(rev*10)+rem#7|(7*10)+6=76|(76*10)+5=765
    n//=10#discard the last digit 56|5|0
    print(rev)
