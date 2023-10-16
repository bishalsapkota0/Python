def isLeapYear(year):
    if(year<=0):
       print("Enter the year again")
    leapYear = False;
    if( year%4 ==0 and (year %100!= 0 or year %400 == 0)):
        leapYear = True
    return leapYear
def main():
    year = int(input("Enter a year : "))
    if(isLeapYear(year)==True):
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")
main()
