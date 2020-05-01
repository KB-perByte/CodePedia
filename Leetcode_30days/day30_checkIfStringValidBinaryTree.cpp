/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
   bool dfs(TreeNode* node, vector<int> &arr, int pos) {
    if (pos > arr.size() - 1) return false;
    // leaf
    if (!node->left && !node->right) {
        return (pos == arr.size() - 1 && node->val == arr[pos]);
    }
    // non-leaf
    if (node->val != arr[pos]) return false;
    bool flag = 0;
    if (node->left) flag = dfs(node->left, arr, pos+1);
    if (node->right) flag = flag || dfs(node->right, arr, pos+1);
    return flag;
}
bool isValidSequence(TreeNode* root, vector<int>& arr) {
    return dfs(root, arr, 0);
}
};