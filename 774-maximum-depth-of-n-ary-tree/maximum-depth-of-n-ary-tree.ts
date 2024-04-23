/**
 * Definition for Node.
 * class Node {
 *     val: number
 *     children: Node[]
 *     constructor(val?: number, children?: Node[]) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.children = (children===undefined ? [] : children)
 *     }
 * }
 */

function maxDepth(root: Node | null): number {
    if (!root){
        return 0;
    }
    let depth : number = 1;
    let queue: Node[] = [];
    queue.push(root);
    queue.push(null);
    while(queue){
        let curr: Node = queue.shift();
        if(!curr){
            if(queue.length == 0){
                break;
            }
            depth+=1;
            queue.push(null);
        }else{
            for(let runner = 0; runner < curr.children.length; runner += 1){
                queue.push(curr.children[runner]);
            }
        }
    }
    return depth;
};