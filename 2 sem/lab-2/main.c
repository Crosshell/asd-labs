#include <stdio.h>
#include <stdlib.h>

typedef struct linked_list {
    double info;
    struct linked_list *next_p;
} l_list;


l_list *l_list_init(double item) {
    l_list *newNode = (l_list*)malloc(sizeof(l_list));
    newNode->info = item;
    newNode->next_p = NULL;
    return newNode;
}

l_list *add_list(l_list *current, double info){
    l_list *newNode = l_list_init(info);
    newNode->next_p = current;
    return newNode;
}

l_list *input_list(int n) {
    if (n % 2 || n == 0){
        printf("ERROR! n must be a pair number\n");
        return NULL;
    }
    double item;
    l_list *head = NULL;

    for (int i = 0; i < n; i++){
        printf("Enter the num for node %d: ", i + 1);
        scanf("%lf", &item);
        head = add_list(head, item);
    }

    return head;
}

void print_list(l_list *head) {
    l_list *current = head;
    while (current != NULL) {
        printf("%lf -> ", current->info);
        current = current->next_p;
    }
}

double multiply_list(l_list *head) {
    double result = 1;
    l_list *current = head;
    l_list *end = head;
    int count = 0;


    while (end->next_p != NULL) {
        end = end->next_p;
        count++;
    }

    for (int i = 0; i < count / 2; i++) {
        double start_val = current->info;
        double end_val = end->info;
        result *= (start_val - end_val);

        current = current->next_p;

        l_list *temp = head;
        while (temp->next_p != end) {
            temp = temp->next_p;
        }
        end = temp;
    }

    return result;
}


void clear_list(l_list *start) {
    if(!start) return;
    l_list *currentNode;
    while (start) {
        currentNode = start;
        start = start->next_p;
        free(currentNode);
    }
}

int main() {
    int n;
    printf("Enter the number of list items(2n): ");
    scanf("%d", &n);

    l_list *start = input_list(n);

    printf("List elements:\n");
    print_list(start);

    double result = multiply_list(start);
    printf("result = %lf\n", result);

    clear_list(start);

    return 0;
}