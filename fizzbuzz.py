def fizzBuzz(int1:int):
    if int1%3 ==0 and int1%5==0:
        print("FizzBuzz")
    elif int1%3 ==0 :
        print("Fizz")
    elif int1%5 ==0 :
        print("Buzz")
    else:
        print(f"{int1}")

for i in range(0,100):
    fizzBuzz(i)