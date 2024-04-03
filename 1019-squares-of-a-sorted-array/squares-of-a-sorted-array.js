/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let i = 0
    let j = nums.length - 1
    let ans = new Array(nums.length)
    let k = ans.length - 1
    while(k>=0){
        if (nums[j] ** 2 > nums[i] **2){
            ans[k] = nums[j] ** 2 
            j--
            k--
        }else{
            ans[k] = nums[i] ** 2
            i++
            k--
        }
    }
    return ans
};