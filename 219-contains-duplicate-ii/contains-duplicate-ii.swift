class Solution {
    func containsNearbyDuplicate(_ nums: [Int], _ k: Int) -> Bool {
        var store: [Int: Int] = [Int: Int]()
        for index in 0..<nums.count{
            guard let curr = store[nums[index]] else {
                store[nums[index]] = index
                continue
            }

            if index - curr <= k {
                return true
            }
            store[nums[index]] = index

        }
        return false
    }
}