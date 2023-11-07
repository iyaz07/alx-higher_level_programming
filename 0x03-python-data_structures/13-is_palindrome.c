#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 *  is_palindrome - prints all elements of a listint_t list
 *  @head: pointer to the start of the list
 *  Return: 1 on true, else false.
 */
int is_palindrome(listint_t **head)
{
	int i, first_half = 0;
	int length = 0;
	int *setArray;
	listint_t *start, *temp;

	if (head == NULL || *head == NULL)
	{
		return (1);
	}
	start = *head;
	temp = *head;

	while (temp != NULL)
	{
		length++;
		temp = temp->next;
	}
	setArray = malloc(length * sizeof(int));

	for (i = 0; i < length; i++)
	{
		setArray[i] = start->n;
		start = start->next;
	}
	for (first_half = 0; first_half < (length / 2); first_half++)
	{
		if (setArray[first_half] != setArray[length - (first_half + 1)])
		{
			free(setArray);
			return (0);
		}
	}
	free(setArray);
	return (1);
}
