class Matrix:
    #constructor
    def __init__(self,grid):
        self.grid = list(grid)
        self.row = len(grid)
        self.col = len(grid[0])
        for g in self.grid:
            if len(g)!=self.col:
                raise ValueError("***Invalid Matrix***")
    #add dunder method
    def __add__(self,other):
        if self.row!=other.row or self.col!=other.col:
            raise ValueError("***Invalid Matrix***")
        final = []
        for i in range(self.row):
            new = []
            for j in range(self.col):
                result = self.grid[i][j]+other.grid[i][j]
                new.append(result)
            final.append(new)
        return Matrix(final)
    #subtract dunder method
    def __sub__(self,other):
        if self.row!=other.row or self.col!=other.col:
            raise ValueError("***Invalid Matrix***")
        final = []
        for i in range(self.row):
            new = []
            for j in range(self.col):
                result = self.grid[i][j]-other.grid[i][j]
                new.append(result)
            final.append(new)
        return Matrix(final)
    #for above add and sub both matrix must be '='
    #multiplication dunder method
    def __mul__(self,other):
        if self.col!=other.row:
            raise ValueError("***Invalid Matrix***")
        final = []
        for i in range(self.row):
            new = []
            for j in range(other.col):
                result = 0
                for k in range(self.col):
                    result += (self.grid[i][k]*other.grid[k][j])
                new.append(result)
            final.append(new)
        return Matrix(final)
    #best way to show result
    def __repr__(self):
        result = ""
        for g in self.grid:
            result += f"{g}\n"
        return result
#method named as numpyClone because later we'ill transform this code into a module...
def numpyClone():
    try:  
        m1 = Matrix([[1,2]])
        m2 = Matrix([[1],[3]])
    except ValueError as v:
        print(v)
    else:
        # print(m1+m2)
        # print(m1-m2)
        print(m1*m2)
#Ensures safety...
if __name__=="__main__":
    numpyClone()