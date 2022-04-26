#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: Pointer to the start of the linked list.
 * @number: Desired number to insert into the sorted linked list.
 * Return: A pointer to the new node or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (node == NULL || number <= node->n)
	{
		new_node->next = node;
		*head = new_node;
		return (new_node);
	}
	else
		while (node != NULL && node->next != NULL && number > node->next->n)
		{
			node = node->next;
		}
	new_node->next = node->next;
	node->next = new_node;
	return (new_node);
}
