#include <stdio.h>
#include <string.h>
#include <cstdlib>



void test();
void tests();
struct ListNode* addcommon(struct ListNode*, struct ListNode*);


struct ListNode{
	int val;
	struct ListNode *next;
};


struct node{
	int val;
	struct node *next;
};



int main(){

	struct ListNode *head1 = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *head2 = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *list1 = head1;
	struct ListNode *list2 = head2;

	list1 -> val = 1;
	list2 -> val = 8;
	list1 -> next = (struct ListNode*)malloc(sizeof(struct ListNode));
	list2 -> next = (struct ListNode*)malloc(sizeof(struct ListNode));
	list1 = list1 -> next;
	list2 = list2 -> next;
	list1 -> val = 2;
	list2 -> val = 5;
	list1 -> next = (struct ListNode*)malloc(sizeof(struct ListNode));
	list2 -> next = (struct ListNode*)malloc(sizeof(struct ListNode));
	list1 = list1 -> next;
	list2 = list2 -> next;
	list1 -> val = 1;
	list2 -> val = 4;
	list1 -> next = NULL;
	list2 -> next = NULL;

	//for (int i = 0; i < 3; i++){
		//list1 = (struct ListNode*)malloc(sizeof(struct ListNode));
		//list2 = (struct ListNode*)malloc(sizeof(struct ListNode));
		//printf("%x\n", list1);
		//printf("%x\n", list2);
		//list1 -> val = i;
		//list2 -> val = 9 - i;
		//list1 = list1 -> next;
		//list2 = list2 -> next;
	//}


	struct ListNode *result = addcommon( head1, head2 );

	while( result != NULL ){
		printf("this is the value of the node: %d\n", result -> val);
		result = result -> next;
	}

	return 0;
}









struct ListNode* addcommon(struct ListNode* l1, struct ListNode* l2){
	int carry = 0, sum = 0;
	struct ListNode *result = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *curr = result;
	result -> val = -1;
	result -> next = NULL;
	while ( l1 != NULL && l2 != NULL ){
		sum = l1 -> val + l2 -> val + carry;
		carry = sum / 10;
		if ( curr -> val < 0 ){ curr -> val = sum % 10; }
		else{
			curr -> next = (struct ListNode*)malloc(sizeof(struct ListNode));
			curr -> next -> val = sum % 10;
			curr -> next -> next = NULL;
			curr = curr -> next;
		}

		l1 = l1 -> next;
		l2 = l2 -> next;
	}

	return result;
}



void test(){
	struct ListNode *node = (struct ListNode*)malloc(sizeof(struct ListNode));
	node -> val = 5;
	node -> next = (struct ListNode*)malloc(sizeof(struct ListNode));
	node -> next -> val = 8;

	printf("another test!\n");
	printf("the value of the first node is: %d\n", node -> val);
	printf("the value of the second node is: %d\n", node -> next -> val);
}




void tests(){

	struct node head = {0, NULL};
	head.next = (struct node*)malloc(sizeof(struct node));
	struct node *ptr = &head;

	*(head.next) = {4, NULL};
	printf("this is the value of the first node: %d\n", head.val);
	printf("this is the value of the second node: %d\n", (*(head.next)).val);


	printf("this is the second part of the experiment: %d\n", ptr -> val);


	printf("this is the third part of the experiment: %d\n", ptr -> next -> val);
	printf("this is the third part of the experiment: %d\n", (ptr -> next) -> val);

	struct node list;
	struct node *listptr;
	listptr = &list;
	printf("this is the fourth part of the experiment: %x\n", &list);
	printf("this is the fourth part of the experiment: %x\n", listptr);
	list = {4, NULL};
	printf("this is the fourth part of the experiment: %x\n", &list);
	printf("this is the fourth part of the experiment: %x\n", listptr);

}
