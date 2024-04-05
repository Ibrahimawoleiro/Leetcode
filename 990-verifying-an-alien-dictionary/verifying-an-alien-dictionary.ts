function isAlienSorted(words: string[], order: string): boolean {

    if (words.length === 1){
        return true
    }

    let dictionary:Record<string, number> = {}

    for (let index in order.split("")){
        dictionary[order[index]] = parseInt(index)
    }
    let max_length: number = 0

    for(let word of words){
        if (word.length > max_length){
            max_length = word.length
        }
    }
    for(let i = 1; i<words.length; i++){
        for(let j = 0; j<max_length; j++){
            if(j>=words[i-1].length || dictionary[words[i-1][j]] < dictionary[words[i][j]]){
                break
            }else if(j >= words[i].length){
                return false
            }else if(dictionary[words[i-1][j]] > dictionary[words[i][j]]){

                return false
            }
        }
    }

    return true
};