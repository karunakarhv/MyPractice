class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanToIntDict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        strSplit = list(s)
        totalSum = 0
        index = 0
        while(index < (len(strSplit))):
            if len(strSplit) == index + 1:
                return totalSum + romanToIntDict[strSplit[index]]
            elif strSplit[index] == 'I' and strSplit[index + 1] == 'V':
                totalSum = totalSum + romanToIntDict[strSplit[index + 1]] - 1
                index = index + 2
            elif strSplit[index] == 'I' and strSplit[index + 1] == 'X':
                totalSum = totalSum + romanToIntDict[strSplit[index + 1]] - 1
                index = index + 2
            elif strSplit[index] == 'X' and strSplit[index + 1] == 'L':
                totalSum = totalSum + romanToIntDict[strSplit[index + 1]] - 10
                index = index + 2
            elif strSplit[index] == 'X' and strSplit[index + 1] == 'C':
                totalSum = totalSum + romanToIntDict[strSplit[index + 1]] - 10
                index = index + 2
            elif strSplit[index] == 'C' and strSplit[index + 1] == 'D':
                totalSum = totalSum + romanToIntDict[strSplit[index + 1]] - 100
                index = index + 2
            elif strSplit[index] == 'C' and strSplit[index + 1] == 'M':
                totalSum = totalSum + romanToIntDict[strSplit[index + 1]] - 100
                index = index + 2
            else:
                totalSum = totalSum + romanToIntDict[strSplit[index]]
                index = index + 1

        return totalSum

if __name__ == "__main__":
    objectTest = Solution()
    print(objectTest.romanToInt('III'))