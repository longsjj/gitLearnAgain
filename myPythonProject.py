class Solution(object):
    """
    this is a 回归求和问题
    """

    def solution(self,arr):

        if len(arr)==1:
            return arr[0]

        return arr[0]+self.solution(arr[1:])
    def solution_sm(self,arr):
        sum =i= 0
        while i<len(arr):
            sum+=arr[i]
            i+=1
        return sum


if __name__ == '__main__':

    sl = Solution()
    v = sl.solution([1,2,3,4,5])
    v1 = sl.solution_sm([1,2,3,4,5])
    print(v,v1)