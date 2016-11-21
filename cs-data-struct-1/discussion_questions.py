"""

Part - 1 Discussion Questions

*************
Runtime
*************


1. When calculating the Big O notation for a particular algorithm,
it’s necessary to consider the length of time it takes for the algorithm
to run as the algorithm’s workload approaches infinity. You can think of the
workload as the number of tasks required to complete a job. What determines
the workload of figuring out whether your box of animal crackers contains
an elephant?

---->The algorithm of figuring out if your box of animal crackers contains
    an elephant is to look through each cracke in the box. So the workload
    here is one task which is check if the next cracker an elephant. Even though
    the animal crackers can be treated as a set (order does not matter here),
    the number of repeated task (checking each cracker) is increased in linear
    direction. So the number of total crackers determines the actual workload
    of completing this job.


2. Order the following runtimes in descending order of efficiency (that is,
    fastest runtimes first, slowest last) as n approaches infinity:
    O(log n)
    O(n2)
    O(n log n)
    O(n)
    O(2n) (i.e. 2 to the n-th power)
    O(1)

---->As n approaches infinity, the order of runtimes in descending order is:
    O(1)
    O(log n)
    O(n)
    O(n log n)
    O(n^2)
    O(2^n)


*****************
Stacks and Queues
*****************


1.In the following cases, would a stack or queue be a more appropriate data structure?

    (1)The process of loading and unloading pallets onto a flatbed truck

----->A stack is more appropriate in this case because the pallet is stacking
      on top of the previous one and you would remove the first from the top.

    (2)Putting bottle caps on bottles of beer as they roll down an assembly line

----->A Queue is more appropriate in this case because each bottle gets in line
        at the back as the assembly line goes and the first bottle gets in line
        will be capped first.

    (3)Calculating the solution to this mathematical expression: 2 + (7 * 4) - (3 / 2)

----->I think a stack is better in this case. To calculate this math expression,
       you would prioritize the math expression in parathesis so you push these
       calculations on top of a stack, and pop them off as solving them. Next you
       would push the next math expression follow by the order of expression and pop
       them of the stack when complete.

2.Describe two more situations where a queue would be an appropriate data structure.

----->(1)Restaurant Lines: first person gets in line will be served first.
      (2)Cars at Red Light: first car waiting at the front goes first when the
                            traffic light turns green.


3.Describe two more situations where a stack would be an appropriate data structure.


----->(1)Packed Elevators: first person goes in the end and the last person gets in the
                    elevator would come out first.
      (2)Doing Dishes: the first dish gets popped last.



*****************
Linked Lists
*****************


1. Given the linked list below, which are the nodes? What is the data for each node?
Where is the head? Where is the tail? (Please be as specific as possible — exactly
which parts of the diagram correspond to each part? Arrows? Boxes? Text?)

----->In the displayed linked list, there are three nodes: apple node, berry node,
      and cherry node. Each node contains a text string and "next" reference to the
      following node the arrow points to. The data for each node is the text string
      of each node ("apple", "berry", and "cherry" in this case). The head is at the
      apple node and there is no tail in this linked list.

2.What’s the difference between doubly- and singly-linked lists?

---->The difference between the two is that doubly-linked list has an extra arrow ("prev")
    that is pointing back to the node before it. It contains two reference arrows,
    one being next and the other being previous.

3.Why is it faster to append to a linked list if we keep track of the tail as an attribute?

---->It is faster because with a tail pointing to the end of a linked list, we know
     where exacty the last node is and so we could append straight to the node where
     the tail is pointing at (kind of like "tail index"?).


*************
Trees
*************


1.Given the tree above, in what order would a Breadth First Search (BFS) algorithm
visit each node until finding burrito (starting at food)? Just list the order of
nodes visited; no need to recreate the state of the algorithm data in your answer.

---->Food-->Italian-->Indian-->Mexican-->lasagna-->pizza-->tikka masala-->saag-->BURRITO


2.Given the tree above, in what order would a Depth First Search (DFS) algorithm
visit each node until finding Chicago-style (starting at food)? Just list the order
of nodes visited; no need to recreate the state of the algorithm data in your answer.

---->Food-->Italian-->lasagna-->pizza-->thin crust-->CHICAGO-STYLE

3.How is a binary search tree different from other trees?

---->A binary search tree is splitting the search into two direction, and with chosen
     to one of the two paths, the workload of the whole search is cut off half by
     eliminating the other half.

"""
