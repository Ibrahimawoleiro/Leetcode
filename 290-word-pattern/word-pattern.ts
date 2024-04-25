function wordPattern(pattern: string, s: string): boolean {
    let pattern_array: string[] = pattern.split('');
    let s_array : string[] = s.split(" ");
    let checker : Set<string> = new Set();
    let store: Map<string, string> = new Map();
    console.log(pattern_array.length)
    console.log(s_array.length)
    if(pattern_array.length != s_array.length){
        return false;
    }
    for(let i  = 0; i < pattern.length; i++){
        if(store.has(pattern_array[i])){
            if (store.get(pattern_array[i]) != s_array[i]){
                return false;
            }else{
                continue;
            }
        }else{
            if(checker.has(s_array[i]) ){
                return false
            }
            checker.add(s_array[i]);
            store.set(pattern_array[i], s_array[i]);
        }
    }
    
    return true;
};