
#include <stdio.h>
#include <string.h>



struct ListNode{
	int val;
	struct ListNode *next;
};



int main(){

	/* declarations */
	struct ListNode list;
	struct ListNode *listptr;
	listptr = &list;

	printf("The initial values of list list:\n");
	printf("value:\t%d\n", (*listptr).val);
	*((*listptr).next) = {4, NULL};
	printf("this is an attempt to try something: %d", (*((*listptr).next)).val );
	printf("next = %d\n", listptr->next);

	int input = 0;
	for (int i = 0; i < 10; i++){
		printf("Enter a number between 0 and 10:\t");
		scanf("%d", input);

		if( listptr == NULL ){ *listptr = {input, NULL}; }
		else{
			struct ListNode node = {input, NULL};
			listptr -> next = &node;
			listptr = listptr -> next;
		}
	}


	listptr = &list;
	while ( listptr != NULL ){
		printf("the value of this node is:\t%d", listptr->val);
		listptr = listptr -> next;
	}

	return 0;
}
