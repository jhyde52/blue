# Takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

def symmetric(s):
    items=len(s)
    column=[]
    digit=0
    while digit<=items:
        i=0
        while i<items:
            j=0
            row= s[i]
           # print row
            while j<items:
                column.append(s[j][i])
                j=j+1
            print column    
            if column !=row:
                return False
            column=[]
            i=i+1
        digit=digit+1
    return True
        
        
                


print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False