# Cracking The Code Interview
# Page #73
# Student: Michael Tocco
# 
# Question:
# We'll underline the elements in common. The arrays are the
# same length and eachhas all distinct elements:
# 
#

def main():
    a = [13,27,35,40,49,55,59]
    b = [17,35,39,40,55,58,60]

    compareArray(a,b)



# basic conditional branching method
def compareArray(a,b):
    sorted = []
    for i in a:
        for j in b:
            if j > i:
                break
            elif j == i: 
                sorted.append(j)
                break
            
    print(sorted)



main()
