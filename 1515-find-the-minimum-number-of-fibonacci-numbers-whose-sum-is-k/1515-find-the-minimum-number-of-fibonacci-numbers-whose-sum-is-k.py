class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        def find_min_fib_nums(k):
            if k < 2:
                return k
            a,b = 1,1
            while b<= k:
                a, b = b, a + b
            return 1 + find_min_fib_nums(k - a)
        return find_min_fib_nums(k)
        
