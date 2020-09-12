/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func deleteNode(root *TreeNode, key int) *TreeNode {
    dummy := &TreeNode{Left:root}
    prev := dummy
    ptr := root
    for ptr != nil && ptr.Val != key {
        prev = ptr
        if ptr.Val > key {
            ptr = ptr.Left
        } else if ptr.Val < key {
            ptr = ptr.Right
        }    
    }
    
    if ptr == nil {
        return root
    }
    
    delete(prev, ptr)
    return dummy.Left
}
