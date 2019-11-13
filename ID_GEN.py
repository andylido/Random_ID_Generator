# Program to generate random numerical id's based on a set interval and digits per interval

# Generates random digits of number
def rand_id(num):
    import random as rd
    L = []
    i = 0
    while i < num:
        L.append(str(rd.randint(0,9)))
        i+=1
    rand4 = ''.join(L)
    return rand4

# Call rand_id function and appends each value into a list. Then returns the list
def interval(num_int, num_dig):
    L = []
    i = 0
    while i < num_int:
        L.append(rand_id(num_dig))
        i += 1
        if i < (num_int):
            L.append("-")
    return L

# Joins the list into a string for the id
def gen_id(x, y):
    rand_id = interval(x, y)
    return ''.join(rand_id)

# Gets user input for length of id    
def getuserinput():
    cont = False
    while cont == False:
        x = input("Number of intervals: ")
        y = input("Number of digits per interval: ")

        try:
            x = int(x)
            y = int(y)
            cont = True
        except ValueError:
            print("Error. Input must be integers.\n")
            
    return gen_id(x,y) #number of intervals, digits per interval

def main():
    print("\nRandom ID Generator\n")
    
    # Loop to let user decide whether to continue or exit program
    cont = True
    resp = "y"
    while cont == True:
        if resp == "y":
            rand_gen_id = getuserinput()
            print("This is your random generated ID:", rand_gen_id)
            resp = input("Continue? (y/n): ")
            print("")
            if resp in ["y","n"]:
                continue
            else:
                resp="n"
            print("")
        elif resp == "n":
            cont = False
            print("Program Exited.\n")
        else:
            cont = True
            print("Program Exited.\n")
main()
