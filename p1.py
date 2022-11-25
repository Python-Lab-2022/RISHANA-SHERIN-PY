import datetime
today=datetime.date.today()
startyear=today.year
finalyear=int(input("what is the final year"))
print("leap years are:")
for year in range(startyear,finalyear):
    if(year%400==0)and(year%100==0):
        print(year)
    elif(year%4==0)and(year%100!=0):
        print(year)
