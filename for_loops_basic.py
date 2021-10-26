# ////////////////////////////////////////////////////////////////////////////
# Subj: Coding Dojo > Python Stack > Python > Fundamentals: For Loops Basic I
# By:   Virgilio D. Cabading Jr.    Created: October 25, 2021
# ////////////////////////////////////////////////////////////////////////////

#   //// FUNCTIONS ///////////////////////////////////////////////////////////

def print_desc(description) :
    print()
    print("////////////////////////////////////////////////////////////////////////////")
    print(description)
    print()

def flexible_counter(low_num, high_num, mult):
    output = ""
    for idx in range (low_num, high_num + 1):
        if idx % mult == 0:
            output += f"{idx} "
    return output


#   //// MAIN EXECUTION SECTION //////////////////////////////////////////////

# ********************************************************
print_desc("1. Basic - Print all integers from 0 to 150")

output = ""
for idx in range(151):
    output += f"{idx} "
else:
    print(output)

# ********************************************************
print_desc("2. Multiples of five - Print all multiples of 5 from 5 to 1000")

output = ""
for idx in range(5,1001,5):
    output += f"{idx} "
else:
    print(output)

# ********************************************************
print_desc("3.Counting the Dojo Way - Print integers 1 to 100.  If divisible by 5 print 'Coding' instead.  If divisible by 10 print 'Coding Dojo'")

output = ""
for idx in range (1,101):
    if idx % 10 == 0:
        output += "Coding Dojo "
    elif idx % 5 == 0:
        output += "Coding "
    else:
        output += f"{idx} "
else:
    print(output)

# ********************************************************
print_desc("4. Whoa. That Sucker's Huge - add odd integers from 0 to 500,000 and print the final sum")

sum = 0
for idx in range (1, 500001, 2):
    sum += idx
print (f"the sum is {sum}")

# ********************************************************
print_desc("5. Countdown by fours - Print positive numbers starting at 2018, counting downj by fours")

output = ""
for idx in range(2018,0,-4):
    output += f"{idx} "
else:
    print(output)

# ********************************************************
print_desc("6. Flexible Counter")

print("if lowNum = 3, and highNum 9, output is " + flexible_counter(2,9,3))