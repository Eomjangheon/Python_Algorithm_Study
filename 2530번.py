hour,minute,second=map(int,input().split())
after_second=int(input())

hour+=after_second//3600
after_second%=3600

minute+=after_second//60
after_second%=60

second+=after_second

if(second>=60):
    minute+=1
    second-=60

if(minute>=60):
    hour+=1
    minute-=60

hour%=24

print("{} {} {}".format(hour,minute,second))