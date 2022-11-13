
import random

def get_random_password(n=8) -> str:
    stroka = 'ABCDEFGHIJKLMNOPQRSTUVWYXZabcdefghijklmnopqrstuvwxyz0123456789'
    listochek = random.sample(stroka, n)
    strochechka = ''.join(listochek)
    return strochechka

    ...  # TODO написать функцию генерации случайных паролей

print(get_random_password())
