#include "lists.h"
/**
 *check_cycle - checks if there is a loop in a Singly Linked List.
 *@list: head of the list..
 *Return: 0 if there is no loop & 1 if there is a loop.
 */
int check_cycle(listint_t *list)
{
	listint_t *usain_bolt = NULL;
	listint_t *me = NULL;

	if (list == NULL)
		return (0);
	usain_bolt = list->next;
	me = list;
	while (usain_bolt && usain_bolt->next != NULL)
	{
		if (usain_bolt == me)
			return (1);
		usain_bolt = usain_bolt->next->next;
		me = me->next;
	}
	return (0);
}
