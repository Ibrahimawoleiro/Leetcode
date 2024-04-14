class Solution {
    func diStringMatch(_ s: String) -> [Int] {
        var j: Int = 0
        var i: Int = s.count
        var ans: [Int] = [Int]()
        var store: Set<Int> = Set<Int>()
        for char in 0..<s.count+1{
            store.insert(char)
        }
        for char in s{
            if char == "I"{
                ans.append(j)
                store.remove(j)
                j+=1
            }else{
                ans.append(i)
                store.remove(i)
                i-=1
            }
        }
        if let rem = store.first{
            ans.append(rem)
        }
        return ans
    }
}