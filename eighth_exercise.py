csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = csv.replace(":", ",").replace(";", ",").split(",")
print(friends_list)