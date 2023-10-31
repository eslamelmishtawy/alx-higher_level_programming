#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - insert_node
 * @list: list
 * @number: n
 *
 * Return: 0
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	while (h && h->next && h->next->n < number)
		h = h->next;

	new->next = h->next;
	h->next = new;
	return (new);
}
