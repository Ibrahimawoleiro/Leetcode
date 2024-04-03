/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func sortedArrayToBST(_ nums: [Int]) -> TreeNode? {
        var high: Int = nums.count - 1
        var low: Int = 0
        return recursive(low, high, array: nums)
    }

    func recursive(_ low:Int, _ high: Int, array nums:[Int]) -> TreeNode?{
        if low > high{
            return nil
        }
        if low == high{
            return TreeNode(nums[high])
        }
        
        var mid: Int = Int((high+low)/2)

        var curr = TreeNode(nums[mid])

        curr.left = recursive(low, mid - 1, array: nums)

        curr.right = recursive(mid + 1, high, array: nums)

        return curr
    }
}