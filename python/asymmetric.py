# Return True if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(s):
    items=len(s)
    column=[]
    digit=0
    while digit<=items:
        i=0
        while i<items:
            j=0
            row= s[i]
            print row
            while j<items:
                column.append(-s[j][i])
                j=j+1
            print column    
            if row != column:
                return False
            column=[]
            i=i+1
        digit=digit+1
    return True

# Test Cases:

print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False
