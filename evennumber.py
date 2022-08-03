print("""
//////////////////////////////////
Create your own number range and 
find out which numbers are even.
//////////////////////////////////
If you want exit the program then 
type "q" in first or second input
But you have to write a value 
in two entries
//////////////////////////////////
""")

while True:
    a = input("First Number:")
    b = input("Second number:")

    if (a == "q" or a == "Q"):
        break

    elif (b == "q" or b == "Q"):
        break

    else:
        a = int(a)
        b = int(b)

        if (a <= b):
            Numlist = list(range(a,b+1))
            even_number = [i for i in Numlist if (i % 2 == 0)]

        else:
            Numlist = list(range(b,a+1))
            even_number = [i for i in Numlist if (i % 2 == 0)]

        print(even_number)