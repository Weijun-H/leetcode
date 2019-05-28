class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:    # 逆时针展开矩阵
        if not matrix : return []
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            next_matrix = []
            print(matrix)
            for x in zip(*matrix):
                next_matrix.append(x)
            print(next_matrix)
            matrix = next_matrix[::-1]
        return res