#include "practice.h"

int numOfDisks; //GLOBAL
char * fromTower, toTower, otherTower;

int main(int argc, char **argv)
{
  int nFibSeqNum = 0;
  if (argc > 1)
    nFibSeqNum = atoi(argv[1]);

  if (nFibSeqNum > 0 || nFibSeqNum < 10)
    numOfDisks = nFibSeqNum;
  else
    numOfDisks = 5;

  if (nFibSeqNum < 0 || nFibSeqNum > 50)
  {
    nFibSeqNum = 0;
    printf ("Input: Invalid, pass number between 0 and 50\n", nFibSeqNum);
  }
  else
    printf ("Input: %d\n", nFibSeqNum);

  printf ("Fibonacci: %d (iterative)\n", fib_iterative(nFibSeqNum));
  printf ("Fibonacci: %d (recursive)\n", fib_recursive(nFibSeqNum));

  printf ("\nNow the Towers of Hanoi, with %d disks:\n\n", numOfDisks);
  fromTower = '1';
  toTower = '3';
  otherTower = '2';

  printf ("\nRecursive, using a stack:\n");
  hanoi_recursive (numOfDisks, 1, 2, 3);
  printf ("\n\nRecursive, no stack:\n");
  hanoi_nostack();
  return 0;
}

unsigned int fib_recursive(unsigned int sequenceNumber)
{
  if (sequenceNumber < 2)
     return sequenceNumber;
  else
     return (fib_recursive(sequenceNumber-1) + fib_recursive(sequenceNumber-2));
}

unsigned int fib_iterative(unsigned int sequenceNumber)
{
  int num1 = 0, num2 = 1;
  if (sequenceNumber > 0)
    while (sequenceNumber != 0)
    {
      unsigned int tmp = num1+num2;
      num1 = num2;
      num2 = tmp;
      sequenceNumber = sequenceNumber - 1;
    }

  return num1;
}

void hanoi_recursive (int nDisks, int pegA, int pegB, int pegC)
{
  if (nDisks > 1)
  {
    hanoi_recursive (nDisks - 1, pegA, pegC, pegB);
    printf ("Now move the top disk from peg %d to peg %d\n", pegA, pegC);
    hanoi_recursive (nDisks-1, pegB, pegA, pegC);
  }
}


void hanoi_nostack()
{
  char *temp;
  if( numOfDisks > 0 )
  {
    numOfDisks = numOfDisks - 1;
    
    temp = otherTower;        //These three lines are there own inverse
    otherTower = toTower;
    toTower = temp;

    hanoi_nostack();

    temp = otherTower;        //See above
    otherTower = toTower;
    toTower = temp;

    printf ("Now move the top disk from peg %c to peg %c\n", fromTower, toTower);

    temp = otherTower;
    otherTower = fromTower;
    fromTower = temp;

    hanoi_nostack();

    temp = otherTower;
    otherTower = fromTower;
    fromTower = temp;

    numOfDisks = numOfDisks + 1;
  }
}

/* Gray <==> binary conversion routines */
// http://www.faqs.org/faqs/ai-faq/genetic/part6/section-1.html

void gray_to_binary (Cg, Cb, n)
/* convert chromosome of length n+1 from Gray code Cg[0...n]
 * to binary code Cb[0...n] */
  unsigned short    *Cg,*Cb;
  int  n;
{
  int j;
  *Cb = *Cg;               /* copy the high-order bit */
  for (j = 0; j < n; j++)
  {
    Cb--; Cg--;         /* for the remaining bits */
    *Cb= *(Cb+1)^*Cg;   /* do the appropriate XOR */
  }
}
void binary_to_gray(Cb, Cg, n)
/* convert chromosome of length n+1 from binary code Cb[0...n]
 * to Gray code Cg[0...n] */
  unsigned short    *Cb, *Cg;
  int  n;
{
  int j;

  *Cg = *Cb;               /* copy the high-order bit */
  for (j = 0; j < n; j++)
  {
    Cg--; Cb--;         /* for the remaining bits */
    *Cg= *(Cb+1)^*Cb;   /* do the appropriate XOR */
  }
}

void reverseLinkedList(void)
{
	typedef struct NODE
	{
	  short data;
	  struct NODE *next;
	} node;

	node *head, *tail;
	if(head==0)
	  return;
	if(head->next==0)
	  return;

	if(head->next==tail)
	{
	  head->next = 0;
	  tail->next = head;
	}
	else
	{
	  node* pre = head;
	  node* cur = head->next;
	  node* curnext = cur->next;
	  head->next = 0;
	  cur->next = head;
	for(; curnext!=0; )
	{
	  cur->next = pre;
	  pre = cur;
	  cur = curnext;
	  if (curnext->next)
            curnext = curnext->next;
	}
	  curnext->next = cur;
	}
}

int factorial_iterative (int number)
{ 
	int rval = 1, i = 1; /* first check input values */ 
	if (number < 0) 
	{ /* we'll return -1 if there's an error */ 
		return (-1); 
	} 
	for (i = number; i > 1; i--) 
	{ 
		rval = rval * i; 
	}
	return (rval); 
}

int factorial_recursive (int number) 
{ 
	if (number < 0) 
	{ /* we'll return -1 if there's an error */ 
		return (-1); 
	} 
	else if ((number == 0) || (number == 1)) 
	{ 
		return (1); 
	} 
	else
	{ 
		return factorial_recursive(number-1) * number; 
	} 
}

int mystrlen (char *ptr) 
{ 
	int i = 0; 
	if (ptr == NULL) { /* the real strlen doesn't handle this */ /* case, but I do! I return -1 */ 
		return (-1); 
	} 
	while (*ptr++) != '\0') 
	{ 
		i++; 
	} 
	return i; 
}
