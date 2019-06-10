/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode *mergeTwoLists(struct ListNode *l1, struct ListNode *l2) {
    struct ListNode *head = NULL, *r = NULL;
    if (l1 && l2) {
        if (l1->val < l2->val) {
            head = l1;
            l1 = l1->next;
        }
        else {
            head = l2;
            l2 = l2->next;
        }
        r = head;
        while (l1 && l2) {
            if (l1->val < l2->val) {
                r->next = l1;
                r = r->next;
                l1 = l1->next;
            }
            else {
                r->next = l2;
                r = r->next;
                l2 = l2->next;
            }
        }
        if (l1) {
            r->next = l1;
        }
        else {
            r->next = l2;
        }
        return head;
    }
    else {
        if (l1) {
            return l1;
        }
        else {
            return l2;
        }
    }
}
