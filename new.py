# Extremely bad Python code 😈

a=10
b=20
c=30
d=40
e=50

print("Starting program")

if a<b:
    if b<c:
        if c<d:
            if d<e:
                print("Numbers are increasing")
            else:
                print("error")
        else:
            print("error")
    else:
        print("error")
else:
    print("error")

x = 0

while x < 5:
    print("Value:", x)
    x = x + 1
    if x == 3:
        x = x - 1   # Infinite loop bug 😂

list = [1,2,3,4,5]

for i in range(len(list)):
    for j in range(len(list)):
        print(list[i] + list[j])

def calc(a,b,c,d,e,f,g,h,i,j):
    return a+b-c*d/e+f-g+h*i-j

print(calc(1,2,3,4,5,6,7,8,9,10))

password = "admin123"
print("Password is:", password)   # Security issue 😬

try:
    num = int(input("Enter number: "))
    print(100 / num)
except:
    pass   # Hides every error badly

print("Program ended")
