class MyHashMap {
    map : Array<list_node>;
    constructor() {
        this.map = new Array(100);
        console.log(this.map);
    }

    put(key: number, value: number): void {
        let hash = key % this.map.length;
        if(this.map[hash] ===undefined){
            this.map[hash] = new list_node(key, value);
            return
        }
        let position: list_node = this.map[hash];
        while(position){
            if (position.key == key){
                position.value = value;
                return
            }
            position = position.next;
        }
        let curr: list_node = new list_node(key, value);
        curr.next = this.map[hash];
        this.map[hash] = curr;
    }

    get(key: number): number {
        let hash: number = key % this.map.length;
        let position: list_node = this.map[hash];
        while(position){
            if (position.key === key){
                return position.value;
            }
            position = position.next;
        }
        return -1;
    }

    remove(key: number): void {
        let hash: number = key % this.map.length;
        let position: list_node = this.map[hash];
        if(!position){
            return 
        }
        if(position.key === key){
            this.map[hash] = position.next
            return
        }
        let previous: list_node = position
        let current : list_node = previous.next
        while(current){
            if (current.key === key){
                previous.next = current.next
                return 
            }
            previous = current
            current = current.next
        }
    }
}


class list_node{
    key: number;
    value: number;
    next: list_node = undefined
    constructor(key: number, value: number){
        this.key = key;
        this.value = value;
    }
}
/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */