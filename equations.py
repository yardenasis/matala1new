def powfun (x:float,i):
    if i==0:
        return 1
    else:
         solution=x
         for z in range(1,i):
             solution = solution*x
    return solution



def assembly (i):
    if i<1:
        return 1
    else:
        solution=i
        for z in range(1,i):
            solution = solution*z
        return solution 
    
    
        
def exponent (x:float):
     solution=1
     for i in  range(1,100):
         solution=solution+(powfun(x,i)) /assembly( i)
     return solution


def absolute(x:float):
    if x>0 :
        return x
    else:
        return x*-1
    
def even (x:float):
    if x%2!=0:
        return True
    else:
        return False
    
 
    
def Ln(x:float):
    if x<=0:
        return 0 
    solution=x-1
    var=0
    while absolute(var-solution)>0.001:
        var=solution
        solution=solution+2*((x-exponent(solution))/ (x+exponent(solution)))
    return solution


def xtimesy (x:float,y:float):
    if x<0:
        return 0.0
    if y==0:
        return 1.0
    elif y==1:
        return float(x)
    else:
        solution=exponent(y*Ln(x))
        return solution


def sqrt (x:float,y:float):
    if y==0:
        return 0.0
    if y<0 and even(x):
        solution=xtimesy(-y, 1/x)
        return -1*solution
    solution=xtimesy(y, 1/x)
    return solution



def calculate(x:float):
    solution=exponent(x)*xtimesy(x,-1)*xtimesy(7,x)*sqrt(x,x)
    return float('%0.6f' % solution)