#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *myhead = *head;

	int count = 0;
	int i;
	int *array;

	while (myhead)
	{
		myhead = myhead->next;
		count++;
	}


	count = count / 2;


	myhead = *head;


	array = malloc(sizeof(int) * count);


	for (i = 0; i < count; i++)
	{
		array[i] = myhead->n;


		myhead = myhead->next;
	}
	i--;
	myhead = *head;
	for (i = 0; i < count; i++)
	{
		if (array[i] != myhead->n)
			return (0);
		myhead = myhead->next;
	}

	return (1);

}
