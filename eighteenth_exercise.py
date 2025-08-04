purchases = [4.25, 8.30,34.50]
def earn_points(price):
    return int(price) * 3

def tier_label(points):
    if points < 100:
        return "Bronze"
    elif points < 500:
        return "Silver"
    else:
        return "Gold"
total_spent = sum(purchases)
total_points = 0

for amount in purchases:
    total_points += earn_points(amount)

final_tier = tier_label(total_points)

print(f"Toplam harcama: ${total_spent:.2f}")
print(f"Toplam puan: {total_points}")
print(f"Seviye: {final_tier}")