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