#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
int getnum(listint_t *head, int i);
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
	int mod = 0;

	if (*head == NULL)
		return (1);

	while (myhead)
	{
		myhead = myhead->next;
		count++;
	}
	mod = count % 2;
	count = count / 2;

	myhead = *head;

	for (i = 0; i < count; i++)
	{
		myhead = myhead->next;
	}
	i--;
	if (mod != 0)
		myhead = myhead->next;
	for (; i >= 0 ; i--)
	{
		if (getnum(*head, i) != myhead->n)
			return (0);
		myhead = myhead->next;
	}
	return (1);
}


int getnum(listint_t *head, int i)
{
	listint_t *hh = head;
	int index = 0;

	for (; index < i; index++)
		hh = hh->next;
	return (hh->n);
}
