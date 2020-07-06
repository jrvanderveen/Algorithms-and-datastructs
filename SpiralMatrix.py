#####
# I: n
# O: a matrix n*n filled in with a spiral patter
# C:
# E: n = 1 return [1]
#####

'''

'''


class Solution(object):

    def generateMatrix(self, n):
        if not n or n == 0:
            return []

        matrix = [[0 for i in range(n)] for i in range(n)]
        left = 0
        right = n-1
        top = 0
        down = n-1
        num = 1
        while left <= right and top <= down:
            for i in range(left, right+1):
                matrix[top][i] = num
                num += 1
            top += 1

            for i in range(top, down+1):
                matrix[i][right] = num
                num += 1
            right -= 1

            for i in range(right, left-1, -1):
                matrix[down][i] = num
                num += 1
            down -= 1

            for i in range(down, top-1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

        return matrix


def printSpiralMatrix(m):
    if len(m[0]) == 0:
        print("Empty matrix")
        return
    print("Matrix of size: " + str(len(m)), end="")
    for row in range(len(m)):
        print("")
        for col in range(len(m[0])):
            print(str(m[row][col]).ljust(2, " "), end=" ")


print("")
printSpiralMatrix(Solution().generateMatrix(1))
print("")
printSpiralMatrix(Solution().generateMatrix(2))
print("")
printSpiralMatrix(Solution().generateMatrix(3))
print("")
printSpiralMatrix(Solution().generateMatrix(4))
