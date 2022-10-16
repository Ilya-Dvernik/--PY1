salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
spended = spend
for total in range(1,months+1):
    total = spended - salary
    spended *= 1+increase
    need_money += total
# TODO Оформить решение

print(round(need_money))
