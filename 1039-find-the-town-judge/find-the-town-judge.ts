function findJudge(n: number, trust: number[][]): number {
    if( n === 1){
        return 1
    }
    let relationship: Record<number, Set<number>> = {}
    const trusted: Set<number> = new Set();
    const trustee: Set<number> = new Set();
    
    for(let tuple of trust){
        trusted.add(tuple[1])
        trustee.add(tuple[0])
        if(!relationship.hasOwnProperty(tuple[1])){
            relationship[tuple[1]] = new Set()
            relationship[tuple[1]].add(tuple[0])
        }else{
            relationship[tuple[1]].add(tuple[0])
        }
    }

    for(let key in relationship){
        if(!trustee.has(Number(key)) && n-1 === relationship[key].size){
            return Number(key)
        }
    }

    return -1;
};