class RecentCounter {
    queue : number[]  = [];
    constructor() {
        
    }

    ping(t: number): number {
        let runner: number = 0;
        this.queue.push(t);
        let left_range: number = t - 3000;
        let right_range: number = t;
        while(runner < this.queue.length){
            if (this.queue[runner] < left_range){
                runner+=1;
            }else{
                break;
            }
        }
        return this.queue.length - runner;
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */