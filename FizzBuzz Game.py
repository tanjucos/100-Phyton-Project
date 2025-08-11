#FizzzBuzz Game

for number in range(1,101):
   if number % 15 == 0:
       print("FizzzBuzz")
   elif number % 3 == 0:
       print("Fizz!")
   elif number % 5 == 0:
       print("Buzz!")
   else:
       print(number)