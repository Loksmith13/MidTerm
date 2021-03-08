print("please enter your birthday")
y=int(input("Year:"))
m=int(input("Month(1-12):")) 
d=int(input("Date:"))
from datetime import date
now = date.today ()

age = date(int(y),int(m), int(d))

print("your age in seconds is " +str((now-age)*84600))