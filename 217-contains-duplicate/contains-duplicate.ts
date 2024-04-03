function containsDuplicate(nums: number[]): boolean {
    let store: Set<number> = new Set()
    let i:number = 0
    while(i < nums.length){
        if(store.has(nums[i])){
            return true
        }
        store.add(nums[i])
        i+=1
    }
    return false
};