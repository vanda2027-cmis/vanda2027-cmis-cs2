def biggest (num, largest):
    if num == "":
        return largest
    elif largest >= float(num):
        num = raw_input ("Next: ")
        return biggest (num, largest)
    elif largest == float(num):
        num = raw_input ("Next: ")
        return biggest (num, largest)
   
        
        
def main():
    ans = biggest (0,0)
    print ans
main()
