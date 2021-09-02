def palin_drome(text):
    return text[::-1]

def palindrome(text):
    return text == palin_drome(text)

b = input('Введите текст: ')

if(palindrome(b)):
    print('это палиндром')