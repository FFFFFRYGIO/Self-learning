def days(n, name):
    j = []
    a = []
    for i in range(n):
        if i == 0:
            j.append(0)
            a.append(1)
        else:
            jx = i - a[j[i-1]]
            j.append(jx)
            ax = i - j[a[i-1]]
            a.append(ax)
    if name == 'john':
        return j
    elif name == 'ann':
        return a

def john(n):
    return days(n, 'john')
    
def ann(n):
    return days(n, 'ann')
    
def sum_john(n):
    return sum(john(n))
    
def sum_ann(n):
    return sum(ann(n))