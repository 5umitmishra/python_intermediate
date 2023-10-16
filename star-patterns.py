""" 1
    1 1
    1 1 1
    1 1 1 1
    1 1 1 1 1 """
i = 1
def pattern(n):
    for i in range (n):
        for j in range(i+1):
            print(1, end=" ")
        print()
pattern(5)
print(" ")



"""     *
     * *
   * * *
 * * * *
* * * * * """
n = 5
for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")

    for j in range(i + 1):
        print("*", end=" ")

    print()
print(' ')




"""     * * * * * 
          * * * * 
            * * * 
              * * 
                *        """
n = 5
for i in range(n):
    for j in range(i):
        print(" ", end=" ")

    for j in range(i, n):
        print("*", end=" ")

    print()
print(" ")




"""       * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * *   """
n = 5
for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")

    for j in range(i + 1):
        print("*", end=" ")
    for j in range(i):
        print("*", end=" ")

    print()
print(" ")



n = 5
for i in range(n):

    for j in range( i+ 1):
        print(" ", end=" ")
    for j in range(i, n-1):
        print("*", end=" ")

    for j in range(i, n):

        print("*", end = " ")
    print()
print(" ")




n = 5
for i in range(n-1):
    for j in range(i,n):
        print(" ", end=" ")

    for j in range(i + 1):
        print("*", end=" ")
    for j in range(i):
        print("*", end=" ")

    print()
n = 5
for i in range(n):

    for j in range( i+ 1):
        print(" ", end=" ")
    for j in range(i, n-1):
        print("*", end=" ")

    for j in range(i, n):

        print("*", end = " ")
    print()
print(" ")



""" 
    * * * * * 
    *       * 
    *       * 
    *       * 
    * * * * * 

    """
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n - 1 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print(" ")


"""

*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
"""
n = 5
for i in range(n):
    for j in range(i +1):
        print("*", end=" ")

    for j in range(i,n -1):
        print("  ", end="  ")
    for j in range(i + 1):
        print("*", end=" ")

    print()
for i in range(n):
    for j in range(i , n):
        print("*", end=" ")

    for j in range(i):
        print("  ", end="  ")
    for j in range(i-1, n -1):
        print("*", end=" " )
    print()










































