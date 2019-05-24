from Sticks_Tree import stree

root = stree((1,1,1,1,1))

print(root)
#The following is an attempt at DFS for the tree 
#we have made
#Create a list
stack = []

stack.append(root)
while(len(stack) != 0):
    s = stack.pop()
    print(s, end = " ")

    #Get all adjacent vertices of the popped vertex s
    i = 0
    while i<len(s.valid_moves):
        stack.append(s.valid_moves[i])
        i += 1

#Now consider a tree traversal which 