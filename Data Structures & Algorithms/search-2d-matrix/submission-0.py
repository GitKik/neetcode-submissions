class Solution:

    def dicot(self, list_:list, target:int) -> bool:
        print(list_)
        
        m_ = len(list_) // 2
        mid = list_[m_]
        if mid == target :
            return True
        elif len(list_) <=1:
            return False
        elif target < mid :
            return self.dicot(list_[:m_],target)
        else :
            return self.dicot(list_[m_:],target)
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in range(1,len(matrix)) :
            if matrix[m][0] > target :
                return self.dicot(matrix[m-1], target)
        return self.dicot(matrix[len(matrix) - 1], target)