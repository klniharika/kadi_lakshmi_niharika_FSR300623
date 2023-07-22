def isDigitSumPalindrome(N):
    pnsum=0
    pnrev=0
    pn=str(N)
    pnsplit=pn.split()
    for i in pn:
        np=int(i)
        pnsum+=np
    npsum=pnsum
    while(pnsum>0):
        rem=pnsum%10
        pnrev=pnrev*10+rem
        pnsum//=10
    if(npsum==pnrev):
        pn9=1
    else:
        pn9=0
    return pn9
pnpal=int(input())
pnresult=isDigitSumPalindrome(pnpal)

