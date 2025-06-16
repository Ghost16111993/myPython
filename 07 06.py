def greeting():
     name = input("Введите ваше имя: ")
     print("Настя")Больше действий
     print(f"Привет {name}, добро пожаловать!")
     print("Настя")

 greeting()

 def summa(a, b):
     c = a + b
     return c

 print(summa(2, 2))

 result = summa(5, 5) - summa(1, 1) - summa(3,3) * summa(2,6)
 print(result)

 def f(a):
     global b
     b += 3
     print(a + b)

 b = 2
 f(b)