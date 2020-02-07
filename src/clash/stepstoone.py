n=130
q=n
r=0
while q!=1:
    r=r+1
    if q%2!=0:
        q=3*q+1
    else:
        q=q/2
print('f=' + str(r))