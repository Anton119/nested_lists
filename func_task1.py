'''Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат проверки.

Сложным паролем будет считаться комбинация символов, в которой :

Есть хотя бы 3 цифры
Есть хотя бы одна заглавная буква 
Есть хотя бы один символ из следующего набора "!@#$%*"
Общая длина не менее 10 символов
Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password", в противном случае - "Easy peasy"

Вам необходимо написать только определение функции check_password

Sample Input 2:

Qwerty1357!
Sample Output 2:

Perfect password
'''

pwd = "Qwerty1357!"
def check_password(pwd):
    f = 0
    upper = 0
    sym = 0
    length = 0
    for i in pwd:
        if i.isdigit():
            f += 1
    
    for i in pwd:
        if i.isupper():
            upper += 1 
    
    for i in pwd:
        if '!' in i or '@' in i or '#' in i or '$' in i or '%' in i or '*' in i:
           sym += 1 
    
    if len(pwd) >= 10:
        length += 1 
    
    if f > 0 and upper > 0 and sym > 0 and length > 0:
        print('Perfect password')
    else:
        print('Easy peasy')
    
check_password(pwd)
