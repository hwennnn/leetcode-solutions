/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int getDecimalValue(ListNode* head) {
        if (head == nullptr) return 0;
        int total = 0;
        
        while (head){
            total <<= 1;
            total |= head->val;
            head = head->next;
        }
        
        return total;
    }
    
};