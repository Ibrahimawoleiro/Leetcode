function containsDuplicate(nums: number[]): boolean {
    // //1
    // let store: Set<number> = new Set()
    // let i:number = 0
    // while(i < nums.length){
    //     if(store.has(nums[i])){
    //         return true
    //     }
    //     store.add(nums[i])
    //     i+=1
    // }
    // return false

    if (nums.length == 1){
        return false
    }

    nums.sort()

    let i: number | String = 0
    let j: number | boolean = 1
    while(j< nums.length){
        if (nums[i] === nums[j]){
            return true
        }
        i+=1
        j+=1
    }
    return false
};