money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
total = money_capital-spend
month=0
spended = 0
while total + spended > 0:
    spended = salary - spend
    total += spended
    spend *= 1.05
    month += 1  # количество месяцев, которое можно прожить

# TODO Оформить решение

print(month)
