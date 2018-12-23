# Working with Loops

def prime(x):

  count=0	

  for i in range(2,(x//2)+1):

    if(x%i==0):
      count+=1

  if count==0:
  	print("Number is prime")
  
  else:
    print(x)   


for i in range(1,21):
  
  if i%3==0 and i%5==0:
    print("FizzBuzz")

  elif i%5==0:
    print("Buzz")

  elif i%3==0:
    print("Fizz")
   
  else:
    prime(i)
  







