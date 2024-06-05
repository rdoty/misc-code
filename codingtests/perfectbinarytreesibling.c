#include <stdio.h>
#include <stdlib.h>

/********************************************************************
 *  MIT License
 *  Copyright (c) 2017 Rick Doty
 *
 * Name: connect
 * Created: 2006.10.25 by Rick Doty
 * Assumes: passed value is the root in a perfectly balanced binary tree.  The
 *  root node's parent node is NULL, and the leaf nodes' child nodes are NULL.
 * Results: All nodes in the tree below the point passed in are assigned
 *  their proper rightSibling attribute
 * Last Modified: 2006.10.25 by Rick Doty (see source control...)
 */

typedef struct _node
{
  short value;
  struct _node *leftChild;
  struct _node *rightChild;
  struct _node *parent;
  struct _node *rightSibling;
} node;

void connect(node *n);

int main(int argc, char **argv)
{
  node tree; // Build the tree of nodes... et cetera...
  // Now create the connections to the right siblings
  // connect(tree);
}

void connect(node *n)
{
  // 061025-RD-I choose a preorder traversal because we
  // want each node processed before any of its children.
  if (n != NULL && n->parent != NULL && n->parent->leftChild == n)
  {
    // 061025-RD-n is on the left and its sibling shares the same parent.
    // Otherwise, isn't this really a cousin (or neighbor)?  ;-)
    n->rightSibling = n->parent->rightChild;
  }
  else
  {
    if (n == NULL)
    {
      // RD-End of the road (branch) - so no sibling
      return;
    }
    else if (n->parent != NULL && n->parent->rightSibling != NULL)
    {
      // RD-In theory, this is the only other condition possible.
      // Find our cousin/neighbor (parent's sibling's child)
      n->rightSibling = n->parent->rightSibling->leftChild;
    }
    else
      n->rightSibling = NULL;
  }
  // printf("Value: %d\n", n->value);

  connect(n->leftChild);
  connect(n->rightChild);
}

//<!---
/* Other ideas, made or found */

unsigned char nodeIsLeft(node *node)
{
  unsigned char isLeftNode = 0;
  if (node && node->parent && node->parent->leftChild == node)
    isLeftNode = 1;
  return isLeftNode;
}

void connect_2(node *n)
{
  node *parent = 0;
  if (n)
  {
    if (n->parent)
    {
      parent = n->parent;
      if (nodeIsLeft(n))
      {
        n->rightSibling = parent->rightChild;
      }
      else
      {
        if (parent->rightSibling)
        {
          n->rightSibling = parent->rightSibling->leftChild;
        }
        else
        {
          // rightmost edge
          n->rightSibling = 0;
        }
      }
    }
    else
    {
      // it's root
      n->rightSibling = 0;
    }
  }
  connect_2(n->leftChild);
  connect_2(n->rightChild);
}
//-->
