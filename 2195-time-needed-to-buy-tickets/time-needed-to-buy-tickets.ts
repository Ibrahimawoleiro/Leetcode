function timeRequiredToBuy(tickets: number[], k: number): number {
    let queue : Array<Map<string, number>> = [];
    for(let i =  0; i <tickets.length; i++){
        if(i != k){
            let curr: Map<string,number> = new Map<string,number>();
            curr.set('Dummy',tickets[i]);
            queue.push(curr);
        }else{
            let curr: Map<string,number> = new Map<string,number>();
            curr.set('Target',tickets[i]);
            queue.push(curr);
        }
    }
    let result: number = 0;
    while(queue.length > 0){
        let current : Map<string, number> = queue.shift();
        result += 1;
        if (current.has('Dummy')){
            let freq: number = current.get('Dummy');
            freq--;
            if(freq == 0){
                current.delete('Dummy')
            }else{
                current.set('Dummy', freq);
                queue.push(current)
            } 
        }else{
            let freq: number = current.get('Target');
            freq--;
            if(freq == 0){
                break;
            }else{
                current.set('Target', freq);
                queue.push(current)
            } 
        }
    }
    return result;
};