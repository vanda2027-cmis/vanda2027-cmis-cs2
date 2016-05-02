def biggest (num):
    new = raw_input ("Next: ")
    if new == "":
		return num
    elif float(new) > float(num):
        return biggest (float(new))
    elif num > float(new):
        return biggest(num)

def main():
	ans = biggest (-float("inf"))
	print ans
main()

def smallest (num):
    new = raw_input ("Next: ")
    if new == "":
        return num
    elif float(new) < float(num):
        return smallest (float(new))
    elif float(num) < float(new):
        return smallest(float(num))

def main():
    ans = smallest (float("inf"))
    print ans
main()

def pow(x,n):
    if n == 1
        return x
    else:
        return x * pow(x, n-1)



   
        
        

