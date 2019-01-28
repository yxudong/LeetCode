/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *p1 = l1, *p2 = l2;
    struct ListNode *newList = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *r = newList;
    int flag = 0;
    
    while(p1!=NULL && p2 != NULL){
        struct ListNode *new = (struct ListNode *)malloc(sizeof(struct ListNode));
        new->val = p1->val + p2 -> val;
        if(flag){
            new -> val += 1;
            flag = 0;
        } // 如果前面有进位加 1 并重置 flag
        if (new -> val > 9){
            flag = 1;
            new->val -= 10;
        } // 如果大于 9 进位
        r -> next = new;
        new -> next = NULL;
        r = new;
        p1 = p1 -> next;
        p2 = p2 -> next;
    }

    // ***********
    while (p1){
        struct ListNode *new = (struct ListNode *)malloc(sizeof(struct ListNode));
        new->val = p1 -> val;
        if(flag){
            new -> val += 1;
            flag = 0;
        } // 如果前面有进位加 1 并重置 flag
        if (new -> val > 9){
            flag = 1;
            new->val -= 10;
        } // 如果大于 9 进位
        r -> next = new;
        new -> next = NULL;
        r = new;
        p1 = p1 -> next;
    }
    
    while (p2){
        struct ListNode *new = (struct ListNode *)malloc(sizeof(struct ListNode));
        new->val = p2 -> val;
        if(flag){
            new -> val += 1;
            flag = 0;
        } // 如果前面有进位加 1 并重置 flag
        if (new -> val > 9){
            flag = 1;
            new->val -= 10;
        } // 如果大于 9 进位
        r -> next = new;
        new -> next = NULL;
        r = new;
        p2 = p2 -> next;
    }
    // ***********

    // // ***********处可以用下面代替
    // struct ListNode *res = (p1) ? p1 : p2;
    // while (res){
        // struct ListNode *new = (struct ListNode *)malloc(sizeof(struct ListNode));
        // new->val = res -> val;
        // if(flag){
            // new -> val += 1;
            // flag = 0;
        // } // 如果前面有进位加 1 并重置 flag
        // if (new -> val > 9){
            // flag = 1;
            // new->val -= 10;
        // } // 如果大于 9 进位
        // r -> next = new;
        // new -> next = NULL;
        // r = new;
        // res = res -> next;
    // }
    
    if(flag){
        struct ListNode *new = (struct ListNode *)malloc(sizeof(struct ListNode));
        new->val = 1;
        r -> next = new;
        new -> next = NULL;
    }
    else{
        r -> next = NULL;
    }
    
    struct ListNode *p = newList;
    newList = newList -> next;
    free(p);
    
    return newList;
}