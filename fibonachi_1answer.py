num1 = int(input("plese enter first number: "))
num2 = int(input("plese enter socond number: "))
fibonachi = int(input("plese enter times to repeat number: "))
count = 0

while count!=fibonachi:
    if num1 <= num2:
        num1 += num2
    else:
        num2 += num1
    count+=1

if num1 <= num2:
    print(num2)
else:
    print(num1)





