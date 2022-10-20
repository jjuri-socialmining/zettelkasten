---
title: Generice swap function by void pointer and memcpy in c
UID: 221020231925
created: 20-Oct-2022
tags:
  - 'created/2022/Oct/20'
  - 'howto'
aliases:
  - 
publish: False
---
## Notes:
- [[C Programming|C]]
- [[Generic pointer|void *]]

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void genericSwap(void *a, void *b, int size)
{
    void* tempMem = malloc(size);
	memcpy(tempMem, a, size);
	memcpy(a, b, size);
	memcpy(b, tempMem, size);
	free(tempMem);
}

int main()
{
    int a = 10;
    int b = 20;

    printf("Before: a = %d, b = %d\n", a, b);
    genericSwap(&a, &b, sizeof(a));
    printf("After:  a = %d, b = %d\n", a, b);

    return 0;
}

```