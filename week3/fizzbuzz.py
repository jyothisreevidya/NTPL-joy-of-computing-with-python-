
def fizz_buzz(n):
    
    for i in range(n):
        if i%3 == 0 and i%5 == 0:
            print(str(i) + " = Fizz_Buzz")
            
        elif i%3 == 0:
            print(str(i) + " = Fizz")
        
        elif i%5 == 0:
            print(str(i) + " = Buzz")
            
        else:
            print(i)

fizz_buzz(20)