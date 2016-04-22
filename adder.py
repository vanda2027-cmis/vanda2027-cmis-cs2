def adder(num,total):
    if num == "":
        return "The sum is " + str(total)
    else:
        total += float(num)
        num = raw_input("Running total: " + str(total) + "\nNext number: ")
        return adder (num, total)
def main():
    ans = adder (0,0)
    print ans
main()
        
        

