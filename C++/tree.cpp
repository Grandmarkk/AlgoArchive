#include <vector>

/**
 * @brief Class representing a binary tree node
 */
class TreeNode
{
public:
    TreeNode *left;
    TreeNode *right;
    int val;

    TreeNode()
    {
        val = -1;
        left = nullptr;
        right = nullptr;
    }

    TreeNode(int val)
    {
        this->val = val;
        left = nullptr;
        right = nullptr;
    }
};

/**
 * @brief Binary search tree
 */
class BST
{
public:
    TreeNode *root;

    BST(int val)
    {
        this->root = new TreeNode(val);
        this->elmNum = 1;
    }

    BST(TreeNode *node)
    {
        this->root = node;
        this->elmNum = 1;
    }

    bool isEmpty()
    {
        return elmNum == 0;
    }

    int size()
    {
        return elmNum;
    }

    int min(TreeNode *root)
    {
        if (!root)
        {
            return -1;
        }
        TreeNode *cur = root;
        while (cur->left)
        {
            cur = cur->left;
        }
        return cur->val;
    }

    int max(TreeNode *root)
    {
        if (!root)
        {
            return -1;
        }
        TreeNode *cur = root;
        while (cur->right)
        {
            cur = cur->right;
        }
        return cur->val;
    }

    int height()
    {
        return heightHelper(root);
    }

    bool search(int val)
    {
        if (!root)
        {
            return false;
        }
        TreeNode *cur = root;
        while (cur)
        {
            if (cur->val == val)
            {
                return true;
            }
            else if (cur->val > val)
            {
                cur = cur->left;
            }
            else
            {
                cur = cur->right;
            }
        }
        return false;
    }

    void insert(int val)
    {
        if (search(val))
        {
            return;
        }
        TreeNode *cur = root;
        while (cur)
        {
            if (cur->val > val)
            {
                if (!cur->left)
                {
                    cur->left = new TreeNode(val);
                    elmNum++;
                    return;
                }
                cur = cur->left;
            }
            else
            {
                if (!cur->right)
                {
                    cur->right = new TreeNode(val);
                    elmNum++;
                    return;
                }
                cur = cur->right;
            }
        }
    }

    void remove(int val)
    {
        this->root = removeHelper(this->root, val);
    }

private:
    int elmNum;

    int heightHelper(TreeNode *root)
    {
        if (!root)
        {
            return 0;
        }
        return 1 + std::max(heightHelper(root->left), heightHelper(root->right));
    }

    TreeNode *removeHelper(TreeNode *root, int val)
    {
        if (!root)
        {
            return nullptr; // Base case: Node not found
        }

        if (val < root->val)
        {
            root->left = removeHelper(root->left, val); // Recur on the left subtree
        }
        else if (val > root->val)
        {
            root->right = removeHelper(root->right, val); // Recur on the right subtree
        }
        else
        {
            // Node to be deleted found
            if (!root->left && !root->right)
            {
                // Case 1: No children (leaf node)
                delete root;
                elmNum--;
                return nullptr;
            }
            else if (!root->left)
            {
                // Case 2: Only right child
                TreeNode *temp = root->right;
                delete root;
                elmNum--;
                return temp;
            }
            else if (!root->right)
            {
                // Case 3: Only left child
                TreeNode *temp = root->left;
                delete root;
                elmNum--;
                return temp;
            }
            else
            {
                // Case 4: Two children
                int maxVal = max(root->left);                  // Find the max value in the left subtree
                root->val = maxVal;                            // Replace the value of the current node
                root->left = removeHelper(root->left, maxVal); // Remove the max value node
            }
        }
        return root; // Return the updated subtree
    }
};
