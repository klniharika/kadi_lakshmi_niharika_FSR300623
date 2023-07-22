def isDigitSumPalindrome(N):  
    pnrev=0
    npsum=N
    while(npsum>0):
        rem=npsum%10
        pnrev=pnrev*10+rem
        npsum=npsum//10
    if(N==pnrev):
        return "yes"
    else:
        return "No"
pnpal=int(input())
pnresult=isDigitSumPalindrome(pnpal)

