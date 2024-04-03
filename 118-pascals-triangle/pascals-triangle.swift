class Solution {
    func generate(_ numRows: Int) -> [[Int]] {
        var ans: [[Int]] = [[Int]]()
        recursive(&ans, numRows)
        return ans
    }

    func recursive(_ ans:inout [[Int]], _ level:Int) -> Void{
        if level == 1{
            ans.append([1])
            return
        }
        recursive(&ans,level - 1)
        var curr:[Int] = Array(repeating: 0, count:level)
        for index in stride(from:0 , to: curr.count, by: 1){
            if index == 0 || index == curr.count - 1{
                curr[index] = 1
            }else{
                if let lastarr = ans.last{
                    var left_upper: Int = index - 1 >= 0 ? lastarr[index - 1] : 0
                    var right_upper: Int = index < lastarr.count ? lastarr[index] : 0
                    curr[index] = left_upper + right_upper
                } 
            }
        }
        ans.append(curr)
    }
}