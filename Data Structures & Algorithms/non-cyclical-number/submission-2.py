class Solution:
    def isHappy(self, n: int) -> bool:

        sums =set()
        loop = True
        while(loop):
            sum = 0
            for num in (list(str(n))):
                number = int(num)
                sum += number ** 2
            if sum == 1:
                return True
            else:
                if sum not in sums:
                    sums.add(sum)
                    n= sum
                else:
                    return False



        