#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if there is a cycle
 * @list: pointer
 * Return: 0
 */

int check_cycle(listint_t *list)
{
	listint_t *lyst, *check;

	if (list == NULL || list->next == NULL)
		return (0);
	lyst = list;
	check = lyst->next;

	while (lyst != NULL && check->next != NULL
		&& check->next->next != NULL)
	{
		if (lyst == check)
			return (1);
		lyst = lyst->next;
		check = check->next->next;
	}
	return (0);
}
