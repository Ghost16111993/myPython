letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
result = ''
for letter in letters:
     if letter.islower():
         result += letter
 print(result)

secret_list = ["Мавпродош", "Лорнектиф", "Древерол", "Фиригарпиг", "Клодобродыч"]
 while True:
     nickname = input("Для входа введите ваш никнейм: ")
     if nickname in secret_list:
         print(f"Ты – свой. Приветствую, любезный {nickname}!")
         break
     else:
          print("Тут ничего нет. Еще есть вопросы?")