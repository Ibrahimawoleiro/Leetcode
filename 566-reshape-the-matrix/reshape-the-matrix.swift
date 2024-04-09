class Solution {
    func matrixReshape(_ mat: [[Int]], _ r: Int, _ c: Int) -> [[Int]] {
        if r * c != mat.count * mat[0].count{
            return mat
        }
        var ans: [[Int]] = Array(repeating: Array(repeating:0 , count:c ) , count: r)
        var ans_row_iterator: Int = 0
        var ans_col_iterator: Int = 0
        for row_index in 0..<mat.count{
            for col_index in 0..<mat[0].count{
                ans[ans_row_iterator][ans_col_iterator] = mat[row_index][col_index]
                ans_col_iterator+=1
                if ans_col_iterator == ans[0].count{
                    ans_col_iterator = 0
                    ans_row_iterator+=1
                }
            }
        }
        return ans
    }
}