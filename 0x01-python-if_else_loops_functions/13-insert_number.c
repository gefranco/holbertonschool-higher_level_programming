#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - insert a node in alinked list
 * @head: the pointer to the head of the list
 * @number: the number to insert in the node
 * Return: the node created
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *list_tmp = *head;
	listint_t *list = list_tmp->next;
	listint_t *end;

	if (number < list_tmp->n || *head == NULL)
	{
		listint_t *insert = malloc(sizeof(listint_t));
		*head = insert;
		insert->next = list_tmp;
		insert->n = number;
		return (insert);
	}
	while (list)
	{
		if (number < list->n)
		{
			listint_t *insert = malloc(sizeof(listint_t));

			list_tmp->next = insert;
			insert->next = list;
			insert->n = number;
			return (insert);
		}
		list_tmp = list;
		list = list->next;
	}
	end = malloc(sizeof(listint_t));
	list_tmp->next = end;
	end->next = NULL;
	end->n = number;
	return (end);
}
