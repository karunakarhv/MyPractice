class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        current = strs[0]
        for i in range(1, len(strs)):
            temp = ""
            if len(strs[0]) == 0:
                break
            for j in range(len(strs[i])):
                if j < len(current) and current[j] == strs[i][j]:
                    temp += current[j]
                else:
                    break
            current = temp
        return current

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        myList = []
        for i in range(len(nums)-1):
            # One of the combinations
            if (i + 1 >= len(nums)) or (i+2 >= len(nums)):
                return myList
            if ((nums[i] + nums[i+1] + nums[i+2]) == 0):
                myList.append([nums[i], nums[i+1], nums[i+2]])
        return myList

if __name__ == "__main__":
    obj = Solution()
    strs = ["flower", "flow", "flight"]
    print(obj.longestCommonPrefix(strs))
    nums = [-1,0,1,2,-1,-4]
    # Numbers sort
    # [-4, -1, -1, 0, 1, 2]
    # -4 compared with -1 and -1
    # -4 compared with -1 and 0
    # -4 compared with 0 and 1
    # -4 compared with 1 and 2
    # -1 compared with -1 and 0
    # -1 compared with 0 and 1 -- break
    # -1 compared with 0 and 1 -- break
    # 0 comapred with 1 and 2
    # -4 and -1 compared with -1
    # -4 and -1 compared with 0
    # -4 and -1 compared with
    print(obj.threeSum(nums))