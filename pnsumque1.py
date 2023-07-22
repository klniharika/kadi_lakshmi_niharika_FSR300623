def sum(Arr,N):
    pnsum=0
    for i in range(N):
        Arr.append(int(input()))
    for i in range(N):
        pnsum+=Arr[i]
    return pnsum
pnarr=[]
pn=int(input())
pnresult=sum(pnarr,pn)

        
