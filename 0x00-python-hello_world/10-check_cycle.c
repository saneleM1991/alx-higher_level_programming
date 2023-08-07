#include "lists.h"

/**
 * check_cycle - checks if a lst has a cycle in it.
 * @lst: Pointer to head node
 * Return: 0 = no cycle, 1 = there is a cycle
 */
int check_cycle(listint_t *lst)
{
	listint_t *crnt, *chck;

	if (lst == NULL || lst->next == NULL)
		return (0);
	crnt = lst;
	chck = crnt->next;

	while (crnt != NULL && chck->next != NULL && chck->next->next != NULL)
	{
		if (crnt == chck)
			return (1);
		crnt = crnt->next;
		chck = chck->next->next;
	}
	return (0);
}
