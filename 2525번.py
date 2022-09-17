hour,minute=map(int,input().split())
after_minute=int(input())
a_hour=after_minute//60
a_minute=after_minute%60

hour=hour+a_hour
minute=minute+a_minute

if minute>=60:
    hour+=1
    minute-=60

hour%=24
print("{} {}".format(hour,minute))