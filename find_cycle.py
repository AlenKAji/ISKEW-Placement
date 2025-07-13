"""class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

head=Node(1)

node2=Node(2)
node3=Node(3)
head.next=node2
node2.next=node3
node3.next=None
def cycle_search(head):
    fast=slow=head
    while(fast and fast.next):
        fast=fast.next.next
        slow=slow.next
        while(fast==slow):
            return True
    return False
print(cycle_search(head))
"""

visited=set()
edges={}
N=int(input("No. of Nodes"))

for I in range(N):
    a,b=list(map(int,input.split()))
    if a in edges.keys():
        edges[a].append(b)
    else:
        edges[a]=b
