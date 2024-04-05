class Solution {
    func intersection(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        var result : [Int] = [Int]()
        var i : Int = 0
        var j : Int = 0
        var current: Int = -1
        var n1 : [Int] = Array(nums1).sorted()
        var n2 : [Int] = Array(nums2).sorted()
        while(i < n1.count && j < n2.count){
           if n1[i] == n2[j] && n1[i] > current{
            result.append(n1[i])
            current = n1[i]
            i+=1
            j+=1
           }else if n1[i] > n2[j]{
            j+=1
           }else{
            i+=1
           }
        }
        return result
    }
}