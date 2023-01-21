# This is a Python script
a = int(input("Give me a number"))
print("hello",a)
if a >10 :
    print("Number > 10")
    if a < 20:
        print("Number <20")
elif a==10 :
    print("a is 10")
elif a<-0 :
    pass
elif a < -0:
    pass
else:
    print("# < 10")
print("done")

if a:
    pass
#if b:
#    pass
result = ( -1 if a<0 else 1 )
print("a is > 0",result)

print("#"*30)
for i in (1,2,3,4,5):
    print(i,end=' ')
print("!")

for i in range(1,-10,-1):
    print(i, end=' ')
    if i == -2:
        break
else:
    print("done all")

print("!")

while a<100 :
    a+=10 # a = a+10
    if a==70:
        continue
    print(a,end=" ")