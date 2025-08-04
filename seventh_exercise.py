week1 = [5, 8, 6, 7, 4, 10, 3]
week2 = [6, 7, 5, 9, 4, 6]

extra_day = int(input())
week2.append(extra_day)

sales = week1 + week2

best_day = max(sales)
worst_day = min(sales)

profit_per_item = 1.5

profit_best_day = best_day * profit_per_item
profit_worst_day = worst_day * profit_per_item

profit_week1 = sum(week1) * profit_per_item
profit_week2 = sum(week2) * profit_per_item
total_profit = profit_week1 + profit_week2

print("En çok kazandığın gün: {:.2f} $".format(profit_best_day))
print("En az kazandığın gün: {:.2f} $".format(profit_worst_day))
print("1. Hafta: {:.2f} $, 2. Hafta: {:.2f} $, Toplam: {:.2f} $".format(profit_week1, profit_week2, total_profit))