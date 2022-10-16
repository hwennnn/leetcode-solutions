/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *c1 = headA, *c2 = headB;
        
        while (c1 != c2){
            if (c1 == nullptr)
                c1 = headB;
            else
                c1 = c1->next;
            
            if (c2 == nullptr)
                c2 = headA;
            else
                c2 = c2->next;
        }
        
        return c1;
    }
};