def num_days(month):
    list1 = ["jan", "mar", "may", "jul", "aug", "oct", "dec"]
    list2 = ["apr", "jun", "sep", "nov"]
    if month in list1:
        print("Number of days is 31")
    elif month in list2:
        print("Number of days is 30")
    elif month == "feb":
        print("Number of days is 28")

num_days("feb")