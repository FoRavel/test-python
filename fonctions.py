def table7():
    n=1
    while n<11:
        print(n*7, end="")
        n=n+1


def table(p):
    n=1
    while n<11:
        print(n*p, end="")
        n=n+1

for p in range(1,21):
    table(p)
for i in range(20):
    print("caca")

def table(p,d,f):
    for n in range(d,f+1):
        print(n*p)

def aire(l,L):
    a=l*L
    return a
print(aire(2,5))
