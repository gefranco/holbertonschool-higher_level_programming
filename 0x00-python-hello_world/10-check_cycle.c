#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the pointer to the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{

	int i, count;
	listint_t *head = list;
	listint_t *main_head = list;

	count = 0;
	if (list == NULL)
		return (0);

	while (list)
	{
		count++;
		list = list->next;
		head = main_head;
		for (i = 0; i < count; i++)
		{
			if (head == list)
				return (1);
			head = head->next;
		}
	}
	return (0);
}
