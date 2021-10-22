import secrets
#import turtle


n = []      #"drawn" numbers

for i in range(6):
    x = ((secrets.randbelow(1000)%54)+1)
    n.append(x)



for x in n:
    print(x)