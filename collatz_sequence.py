def collatz(number):
    if number%2==0:
        result= number//2
    else:
        result= 3 * number + 1
    print(result)
    return result
    
try:
   number=int(input('enter a positive integer! '))
   if number <=0:
      print(int('Enter a positive integer!'))
   else:
     while number!=1:
        number=collatz(number)
   
except ValueError:
    print('Enter a valid integer!')
    

