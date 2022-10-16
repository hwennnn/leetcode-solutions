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
    bool isPalindrome(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return true;
        
        ListNode *slow = head, *fast = head;
        
        while (fast->next && fast->next->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        
        slow->next = reverseLL(slow->next);
        slow = slow->next;
        
        while (slow){
            if (head->val != slow->val) return false;
            
            head = head->next;
            slow = slow->next;
        }
        
        return true;
        
    }
    
    ListNode* reverseLL(ListNode *node){
        ListNode *res = NULL;
        
        while (node){
            ListNode *next = node->next;
            node->next = res;
            res = node;
            node = next;
        }
        
        return res;
    }
};