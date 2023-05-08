#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - repreents a singly linked list.
 * @n: an integer of the struct.
 * @next: a pointer to the next node in the list.
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

int check_cycle(listint_t *list);
size_t print_listint(const listint_t *head);
listint_t *add_nodeint(listint_t **h, const int n);
void free_listint(listint_t *h);

#endif
