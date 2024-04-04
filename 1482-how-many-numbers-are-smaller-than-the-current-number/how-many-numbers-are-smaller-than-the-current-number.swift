class Solution {
    func smallerNumbersThanCurrent(_ nums: [Int]) -> [Int] {
        // //1
        // var count: Int = 0
        // var result: [Int] = Array(repeating: 0, count: nums.count)
        // for index in 0..<nums.count{
        //     for checker_index in 0..<nums.count{
        //         if index == checker_index{
        //             continue
        //         }
        //         if nums[checker_index] < nums[index]{
        //             count+=1
        //         }
        //     }
        //     result[index] = count
        //     count = 0
        // }
        // return result

        //2
        var count: Int = 0
        var store: [Int: Int] = [:]
        var result: [Int] = Array(repeating: 0, count: nums.count)
        for index in 0..<nums.count{
            for checker_index in 0..<nums.count{
                if index == checker_index{
                    continue
                }else if store.keys.contains(nums[index]){
                    result[index] = store[nums[index]]!
                    
                }
                if nums[checker_index] < nums[index]{
                    count+=1
                }
            }
            store[index] = count
            result[index] = count
            count = 0
        }
        return result
    }
}