class Matrix:
    def __init__(self,list):
        if(validate(list)):
            self.value = list
        else:
            return "This matrix is not a valid matrix"  

    def add(self,matrix_2):
        if(validate_two(self.value,matrix_2)):
            added_list = [[i1+j1 for i1, j1 in zip(i,j)] for i,j in zip(self.value,matrix_2)]
            return added_list

    def subtract(self,matrix_2):
        if(validate_two(self.value,matrix_2)):
            subtracted_list = [[i1-j1 for i1, j1 in zip(i,j)] for i,j in zip(self.value,matrix_2)]
            return subtracted_list

    def multiply(self,matrix_2):
        if(validate(self.value) and validate(matrix_2) and validate_four(self.value,matrix_2)):
            multiplied_list = [[sum(a * b for a, b in zip(row, column))
                        for column in zip(*matrix_2)]
                                for row in self.value]
            # zip(*list) returns the complement of that 2D array in case of nested list 
            # what it does is that it divides the rows and then apply zip to all the rows 
            # giving the previous columns as rows in the new nested list                    
            return multiplied_list

    def exponent(self,power):
        ans = self.value
        for i in range(power - 1):
            ans = self.multiply(ans)
        return ans                                
    
    def determinant(self):
        if(validate_three(self.value)):
           return det(self.value)

def validate(list):
    length = len(list[0])
    for x in list:
        if(len(x)!=length):
            return False
    return True   

def validate_two(list1,list2):
    if(validate(list1) and validate(list2)):
        row1 = len(list1)
        row2 = len(list2)
        column1 = len(list1[0])
        column2 = len(list2[0])
        if(row1 == row2 and column1 == column2):
            return True
    return False

def validate_three(list):
    length = len(list)
    for x in list:
        if(len(x)!=length):
            return False
    return True 

def validate_four(list1,list2):  
    length = len(list1)
    for x in list2:
        if(len(x)!=length):
            return False
    return True          

def cofactor(list , i):
    return list[0][i]*((-1)**(i))

def correspondingSubMatrix(list , i):
    #function to find submatrix
    n = len(list)
    j = 0
    k = 0
    subMatrix = [[0] * (n-1) for k in range(n-1)]
    # subMatrix = [] gives index out of error so instead of that we will have to use falsy values like none 0 or ' '
    #  at every value declaring it
    for x in range(n):
        if(x!=0):
            for y in range(n):
                if(y!=i):
                    subMatrix[j][k] = list[x][y]
                    k+=1
            k=0
            j+=1


    return subMatrix

def det(list):
    n = len(list)
    if(len(list) == 1):
        return list[0]
    if(len(list) == 2):
        return list[0][0]*list[1][1] - list[0][1]*list[1][0]
    deter = 0    
    for i in range(n):
        deter+= cofactor(list,i)*det(correspondingSubMatrix(list,i))
    
    return deter      

         
matrix_obj = Matrix([
[1, 2, 3], 
[4, 5, 6], 
[7, 8, 9]
   ])
matrix_2 = [
[10, 20, 30], 
[40, 50, 60], 
[70, 80, 90]
   ]

print(matrix_obj.determinant())
