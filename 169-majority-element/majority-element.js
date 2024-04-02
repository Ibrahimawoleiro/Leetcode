/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    // //1
    // let dictionary = {}

    // nums.forEach((curr)=>{
    //     if(curr in dictionary){
    //         dictionary[curr]+=1
    //     }else{
    //         dictionary[curr] = 1
    //     }
    // })

    // for(let key in dictionary){
    //     if(dictionary[key] > Math.floor(nums.length/2)){
    //         return key
    //     }
    // }

    //2
    let count = 0
    let curr = 0
    for(let i = 0; i < nums.length;i++){
        if (count == 0){
            count = 1
            curr = nums[i]
            continue
        }
        if (nums[i] == curr){
            count +=1
        }else{
            count -=1
        }
    }
    return curr
};