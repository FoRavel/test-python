ch = "caractère"
for i in range(len(ch)-1):
    print(ch[i]+"*", end="")
print(ch[len(ch)-1])


cha = "sossdfse"
ch2 = ""
for i in cha:
    ch2  = i+ch2
print(ch2)

if ch2 == cha:
    print("c'est un palinfuck")
else:
    print("ce n'est pas un palindrome")
