#include "lists.h"

/**
 * is_palindrome - checks if a list is a palindrome
 *
 * @head: the list.
 *
 * Return: 1 if it is one, 0 if not.
 */

int is_palindrome(listint_t **head)
{
	listint_t *p1, *p2;
	listint_t *mid = NULL;
	int result = 1;

	if (head == NULL)
	{
		return (1);
	}
	if ((*head)->next == NULL)
	{
		return (1);
	}

	p1 = p2 = *head;
	while (p2)
	{
		p2 = p2->next;
		if (p2)
			p2 = p2->next;
		if (p2)
			p1 = p1->next;
	}
	mid = p1;
	reverseList(&(mid->next));
	p1 = *head;
	p2 = mid->next;
	while (result == 1 && p2)
	{
		if (p1->n != p2->n)
			result = 0;
		p1 = p1->next;
		p2 = p2->next;
	}
	reverseList(&(mid->next));
	return (result);
}

/**
 * reverseList - reverses a list
 *
 * @head: the list.
 *
 */

void reverseList(listint_t **head)
{
	listint_t *prev = NULL, *ptr = *head, *temp;

	while (ptr)
	{
		temp = ptr->next;
		ptr->next = prev;
		prev = ptr;
		ptr = temp;
	}
	*head = prev;
}
