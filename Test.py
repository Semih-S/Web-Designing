#!/usr/bin/python3
import cgi, cgitb
from datetime import datetime
import datetime

cgitb.enable()
form = cgi.FieldStorage()
year = form.getvalue("theYear")
val = form.getvalue("radbutton")

def Easter(y):
    y = int(y)
    a = y % 19   
    b = y // 100   
    c = y % 100   
    d = b // 4   
    e = b % 4   
    g = (8 * b + 13) // 25   
    h = (19 * a + b - d - g + 15) % 30   
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32
    
    if n > 9:
        num = (f"{p}/{n}/{y}")
    else:
        num = (f"{p}/0{n}/{y}")

    easter_date = datetime.date(y, n, p)
    if p == 1:
        ver = easter_date.strftime("%d<sup>st</sup> %B %Y")
    elif p == 2:
        ver = easter_date.strftime("%d<sup>nd</sup> %B %Y")
    elif p == 3:
        ver = easter_date.strftime("%d<sup>rd</sup> %B %Y")
    else:
        ver = easter_date.strftime("%d<sup>th</sup> %B %Y")

    if val == "numeric":
        return num
    elif val == "verbal":
        return ver
    else: 
        return f"{num} \n\n\n {ver}"
        
    


print("Content-Type: text/html; charset=utf-8")
print("")
print("<!DOCTYPE html>")
print("<html>")
print('<head>')
print("<title> Your Easter Date </title>")
print('<link rel="stylesheet" type="text/css" href="../Project 2/styleforCGIandFORM.css">')
print("</head>")
print("<body>")
print("<p>")
print("The easter date in year", year, "is:", Easter(year))
print("</p>")
print('<button onclick="history.back()">Go Back</button>')
print("</body>")
print("</html>")
