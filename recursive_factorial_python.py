def factorial( n ):
   if n <1:   # always keep your base case fiest
       return 1
   else:
       res = n * factorial( n - 1 )  
       print str(n) + '! = ' + str(res)
       return res