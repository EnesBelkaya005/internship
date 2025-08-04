total_race_time = input("Enter the total race time: ")
pitstop_num = input("Enter the pitstop number: ")
avg_pitstop_time = input("Enter the average pitstop time: ")

total_pitstop_time = pitstop_num*avg_pitstop_time

percentage_race_spent_time = (total_pitstop_time/total_race_time)*100
percentage_race_spent_time = round(percentage_race_spent_time,2)

print(f"The total pitstop time is {total_pitstop_time} + sn")
print(f"The percentage race spent time is {percentage_race_spent_time}%")
if percentage_race_spent_time > 5:
    print("You need a new pit crew")