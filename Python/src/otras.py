'''
Created on 4 ene. 2021

@author: aleja
'''
def overlapping(l1,l2):
    for elemento in l1:
        if elemento in l2:
            return True
    else:
        return False

print(overlapping([1,4,5,3],  [3,77,88,99]))