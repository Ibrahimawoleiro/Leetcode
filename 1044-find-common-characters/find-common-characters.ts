function commonChars(words: string[]): string[] {
    let current : Record<string, number> = {}
    let checked : Record<string, number> = {}
    let result : string[] = []
    for(let index in words){
        if (parseInt(index) === 0){
            for(let char of words[index]){
                if (!checked.hasOwnProperty(char)){
                    checked[char] = 1
                    continue
                }
                checked[char] += 1
            }
        }

        for(let char of words[index]){
            if (checked.hasOwnProperty(char)){
                checked[char] -= 1
                if(!current.hasOwnProperty(char)){
                    current[char] = 1
                }else{
                    current[char] += 1
                }
                if(checked[char] == 0){
                    delete checked[char]
                }
            }
        }
        checked = current
        current = {}
    }
    console.log(checked)
    Object.entries(checked).forEach(([key,value])=>{
        let i: number = 0;
        while(i < value){
            result.push(key)
            i+=1
        }
    })

    return result
};