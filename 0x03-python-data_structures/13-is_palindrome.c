#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the head of the list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *prev;
	int values[9999], i = 0, c = 0;

	if ((!*head) || (!head))
	{
		return (1);
	}
	prev = *head;
	if (!prev->next)
	{
		return (1);
	}
	while (prev)
	{
		values[i] = prev->n;
		prev = prev->next;
		i++;
	}
	i--;
	while (i >= 0 && c <= i)
	{
		if (values[i] != values[c])
		{
			return (0);
		}
		i--;
		c++;
	}
	return (1);
}
