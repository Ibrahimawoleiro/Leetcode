/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let i = 0
    let j = 0
    while(j < nums.length){
        if (nums[j] > nums[i]){
            nums[i+1] = nums[j]
            i+=1
        }
        j+=1
    }
    return i + 1
};