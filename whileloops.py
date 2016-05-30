def countdown(x):
    while x >= 0:
        print x
        x-=1
countdown(67)

def countdownup(x):
    if x > 0:
        while x >= 0:
            print x
            x-=1
    else:
        while x <=0:
            print x
            x+=1
countdownup (67)
countdownup (-123)
    
def countfrom2 (x, y):
        while x < y:
            print x
            x += 1
        while x > y:   
            print x
            x -= 1
countfrom2 (-10,10)
countfrom2 (12,3)

def sumofodds (n):
    total = 0
    while n > 0:
        if n % 2 == 1:
            total += n
            n -= 1
        else:
            n -= 1
    while n < 0:
        if n % 2 == 1:
            total += n
            n += 1
        else:
            n += 1
    return total
print sumofodds (10)
print sumofodds (-35)

def grid (w, h):
    row = ""
     while h > 0:
        while w > 0:
            row += "."
            w -= 1
        row += "\n"
        h -= 1
    return row 
   
        

print grid (10, 10)
        







