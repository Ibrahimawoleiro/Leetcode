class Solution {
    func getRow(_ rowIndex: Int) -> [Int] {
        var ans: [[Int]] = [[Int]]()
        recursive(&ans, rowIndex)
        guard let last = ans.last else {return [1]}
        return last
    }

    func recursive(_ ans:inout [[Int]], _ level:Int) -> Void{
        print(level)
        if level == 0{
            ans.append([1])
            return
        }
        recursive(&ans,level - 1)
        var curr:[Int] = Array(repeating: 0, count:level+1)
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