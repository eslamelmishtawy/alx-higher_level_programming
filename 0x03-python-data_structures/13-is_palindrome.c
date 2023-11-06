#include "lists.h"
#include <stdio.h>

/**
 * reverse - reverses a linked list
 * @head: h
 *
 * Return: pointer to the first node in the new list
 */
listint_t *reverse(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *h = *head;

	while (h != NULL)
	{
		listint_t *next = h->next;

		h->next = prev;
		prev = h;
		h = next;
	}
	return (prev);
}

/**
 * is_palindrome - p
 * @head: h
 *
 * Return: 0
 */
int is_palindrome(listint_t **head)
{

	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *reversed_list = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	reversed_list = reverse(&slow);
	while (*head != NULL && reversed_list != NULL)
	{
		if ((*head)->n != reversed_list->n)
			return (0);
		*head = (*head)->next;
		reversed_list = reversed_list->next;
	}
	return (1);
}
