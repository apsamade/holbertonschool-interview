# Insert in sorted linked list

Technical interview preparation project.

## Task

Write a function in C that inserts a number into a sorted singly linked list.

- Prototype: `listint_t *insert_node(listint_t **head, int number);`
- Return: the address of the new node, or `NULL` if it failed

## Files

| File | Description |
| ---- | ----------- |
| `0-insert_number.c` | Implementation of `insert_node` |
| `lists.h` | Header file with the `listint_t` structure and function prototypes |

## Compilation

```
gcc -Wall -Werror -Wextra -pedantic 0-main.c linked_lists.c 0-insert_number.c -o insert
```
