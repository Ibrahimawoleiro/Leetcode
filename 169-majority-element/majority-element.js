/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let dictionary = {}

    nums.forEach((curr)=>{
        if(curr in dictionary){
            dictionary[curr]+=1
        }else{
            dictionary[curr] = 1
        }
    })

    for(let key in dictionary){
        if(dictionary[key] > Math.floor(nums.length/2)){
            return key
        }
    }
};