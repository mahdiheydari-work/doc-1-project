num1 = int(input("plese enter first number: "))
num2 = int(input("plese enter socond number: "))
sum = 0
fibonachi = int(input("plese enter times to repeat number: "))


for i in range(fibonachi):
    sum = num1 + num2
    if num1 <= num2:
        num1 = sum 
        print (sum)
    else:
        num2 = sum
        print (sum)


