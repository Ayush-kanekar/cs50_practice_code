months = [ "January", "February", "March", "April", "May", "June",
           "July", "August", "September", "October", "November", "December"
]
def main():
    while True:
        date = input("Date: ").title()
        try:
            ##split "/" 
            if "/" in date:
                month,day,year = date.split("/")
                ##checks if the month is month/13/2009 
                if month.isalpha() == True:
                    continue
            ##splits the ","
            if "," in date:
                date = date.replace(",","")##
                month,day,year = date.split()
                #what if the month is in letter
            if month.isalpha()== True:
                month = months.index(month) + 1 

            day,month,year = int(day),int(month),int(year)

            ##valid dates 
            if year < 1636:
                break
            if not (1 <= month <= 12):
                continue
            if not (1 <= day <=31):
                continue

            print(f"{year}-{month:02}-{day:02}",end="\n")
            break
        except:
            continue



##f










        


main()
