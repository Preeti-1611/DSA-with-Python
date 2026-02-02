def reverse(n,l,r):
    while l<r:
      n[l],n[r]=n[r],n[l]
      l+=1
      r-=1



def rightrotate(n,d):
     n1 = len(n)


     reverse(n,d,n1-1)
     reverse(n,0,n1-d)
     reverse(n,0,n1-1)

     return n


n = [4,1,3,8,7]
print(rightrotate(n,2))