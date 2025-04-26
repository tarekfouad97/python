def fizzBuzz(int1:int):
    """
    Implement the FizzBuzz game logic for a given number.
    
    The function prints:
    - "FizzBuzz" if the number is divisible by both 3 and 5
    - "Fizz" if the number is divisible by 3
    - "Buzz" if the number is divisible by 5
    - The number itself if none of the above conditions are met
    
    Args:
        int1 (int): The number to evaluate
        
    Returns:
        None: The function prints the result based on the FizzBuzz rules
    """
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