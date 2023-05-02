#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Stack{
	int num[10000];
	int here = -1;
}STACK;

STACK sta;

void push(STACK *st, int a);
void pop(STACK *st);
void size(STACK *st);
void empty(STACK *st);
void top(STACK *st);

int main() {
	int i;
	char str[6];
	int push_num;
	scanf("%d", &i);
	for (int j = 0; j < i; j++) {
		scanf("%s", str);
		if (0 == strcmp(str, "push")) {
			scanf("%d", &push_num);
			push(&sta, push_num);
		}
		if (0 == strcmp(str, "pop")) {
			pop(&sta);
			fgetc(stdin);
		}
		if (0 == strcmp(str, "size")) {
			size(&sta);
			fgetc(stdin);
		}
		if (0 == strcmp(str, "empty")) {
			empty(&sta);
			fgetc(stdin);
		}
		if (0 == strcmp(str, "top")) {
			top(&sta);
			fgetc(stdin);
		}
	}
	return 0;
}

void push(STACK* st, int a) {
	st->here++;
	st->num[st->here] = a;
}

//•pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
void pop(STACK *st) {
	if (st->here == -1) {
		printf("-1\n");
	}
	else {
		printf("%d\n", st->num[st -> here]);
		st->num[st->here] = NULL;
		st->here--;
	}

}

//•size: 스택에 들어있는 정수의 개수를 출력한다
void size(STACK *st) {
	int HERE = st->here + 1;
	printf("%d\n", HERE);
}

//•empty: 스택이 비어있으면 1, 아니면 0을 출력한다.

void empty(STACK *st) {
	if (st->here == -1)
		printf("1\n");
	else
		printf("0\n");
}

//•top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

void top(STACK *st) {
	if (st->here == -1)
		printf("-1\n");
	else printf("%d\n", st->num[st->here]);
}
