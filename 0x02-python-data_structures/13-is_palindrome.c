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
	listint_t *p1 = *head;
	listint_t *p2 = *head;

	if (*head == NULL)
		return (1);

	while (p2 && p2->next && p2->next->next)
	{
		p1 = p1->next;
		p2 = p2->next->next;
	}

	p1 = reverseList(&p1);
	p2 = *head;
	while (p1 && p2)
	{
		if (p1->n != p2->n)
			return (0);
		p1 = p1->next;
		p2 = p2->next;
	}

	return (1);
}

/**
 * reverseList - reverses a list
 *
 * @head: the list.
 *
 * Return: head reversed
 */
listint_t *reverseList(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;
	return (*head);
}
