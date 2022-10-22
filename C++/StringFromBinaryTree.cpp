#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <map>
#include <cmath>
#include <conio.h>
#include <queue>
typedef long long ll;
using namespace std;
int main()
{
    getch();
}

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
class Solution
{
public:
    string tree2str(TreeNode *root)
    {
        string ans;
        if(!root)
            return "";
        if(isLeaf(root))
            return to_string(root->val);
        ans+=to_string(root->val);
        ans+="(";
        ans+= tree2str(root->left);
        ans+=")";
        if(root->right)
        {
            ans+="(";
            ans+= tree2str(root->right);
            ans+=")";
        }
        return ans;
    }
    bool isLeaf(TreeNode *root)
    {
        if(!root->left&&!root->right)
            return true;
        return false;
    }
};