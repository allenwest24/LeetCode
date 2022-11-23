/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
    var out [][]int
    if root == nil {
        return out
    }
    
    todo := []*TreeNode{}
    todo = append(todo, root)
    for len(todo) != 0 {
        next_todo := []*TreeNode{}
        all_null := true
        curr_level := []int{}
        for ii := 0; ii < len(todo); ii++ {
            if todo[ii] != nil {
                all_null = false
                curr_level = append(curr_level, todo[ii].Val)
                next_todo = append(next_todo, todo[ii].Left, todo[ii].Right)
            }
        }
        if all_null {
            return out
        }
        out = append(out, curr_level)
        todo = next_todo
    }
    return out
}
