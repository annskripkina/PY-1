salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев


i = 0
while i != months:
    need_money = need_money + spend - salary
    spend = spend + spend * increase
    i += 1

print(round(need_money))
