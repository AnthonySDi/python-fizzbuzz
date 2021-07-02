def fizzBuzz(num):
  ''' 
  Receives num from main and determines if it is divisable by 3, 5, or both and prints the int with fizz, buzz, or fizzbuzz respectfully. 

  helper function to main()

  keyword arguments:
  num: int 
  '''
  if(num % 3 == 0 and num % 5 == 0):
    #num is divisable by both 3 and 5
    print(str(num) + ' fizzbuzz')
  elif(num % 3 == 0):
    #num is divisable by 3 only
    print(str(num) + ' fizz')
  elif(num % 5 == 0):
    #num is divisable by 5 only
    print(str(num) + ' buzz')
  else:
    #num was not divisable by 3 or 5
    print(num)

def main():
  '''
  loops through a range of 1 through 100 and passes each number onto helper function fizzBuzz(num) as an argument
  '''
  for i in range(1,101):
    fizzBuzz(i)

main()