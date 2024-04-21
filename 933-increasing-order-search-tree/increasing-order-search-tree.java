/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode increasingBST(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        this.traversal(root,stack);
        TreeNode curr = null;
        while(!stack.isEmpty()){
            System.out.println(stack.peek().val);
            TreeNode stack_top = stack.pop();
            stack_top.right = curr;
            curr = stack_top;
        }
        return curr;
    }

    public TreeNode traversal(TreeNode node, Stack stack){
        if(node == null){
            return null;
        }
        this.traversal(node.left, stack);
        stack.push(new TreeNode(node.val));
        this.traversal(node.right, stack);
        return null;
    }
}