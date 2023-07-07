a=[1,3,2,2,-4,-6,-2,8]
tv=4
l=[]
l1=[]
for i in a:
    for j in a[1:]:
        if((i+j)==tv):
            if i+j==tv:
                l.append([i,j])
                
l.sort()
print(l[:4])
for k in l[:4]:
    for b in k:
        l1.append(b)
print(l1)

