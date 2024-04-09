class Solution {
    func findErrorNums(_ nums: [Int]) -> [Int] {
        var ans: [Int] = [Int]()
        var store: [Int:Int] = [Int: Int]()
        for number in nums{
            if let curr = store[number]{
                store[number] = curr+1
                ans.append(number)
            }else{
                store[number] = 1
            }
        }
        for number in 1..<nums.count+1{
            guard let curr = store[number] else{
                ans.append(number)
                return ans
            }
        }
        return []
    }
}