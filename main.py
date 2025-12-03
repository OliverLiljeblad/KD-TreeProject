# KD-TREE PROJECT
# Authors: Micki Eustache
# Debugged with ChatGPT

class KDTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class KDTree:
    def __init__(self, k):
        self.root = None
        self.k = k
        self.count = 0

    def insert(self, value):
        # Empty tree
        if self.root == None:
            self.root = KDTNode(value)
            self.count += 1
            return
        
        current = self.root
        depth = 0

        while True:
            # Calculate current depth for axis comparison
            cd = depth % self.k

            # Find proper empty spot for new node and insert it there
            if value[cd] < current.value[cd]:
                if current.left is None:
                    current.left = KDTNode(value)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = KDTNode(value)
                    break
                current = current.right
            
            # Didn't find valid empty spot for insertion at current level
            # Update depth and re-enter while loop
            depth += 1
        self.count += 1

    def __len__(self):
        return self.count
    
    def __contains__(self, value):
        current = self.root
        depth = 0

        while current is not None:
            if value == current.value:
                return True

            cd = depth % self.k

            if value[cd] < current.value[cd]:
                    current = current.left
            else:
                    current = current.right

            depth += 1

        return False
    
    def search(self, value):
        current = self.root
        depth = 0
        cd = depth % self.k

        while value != current.value:
            if value[cd] < current.value[cd]:
                current = current.left
            else:
                current = current.right

        return current
    
    def delete(self, value):
        self.root = self._delete(self.root, value, 0)
        self.count -= 1
    
    def _delete(self, current, value, depth):
        print(f"\n\n===========Deleting: {value} at depth {depth}==============")
        print(f"Current: {current.value}")
        # Return none if node not found        
        if not current:
            return None

        cd = depth % self.k
        print(f"CD: {cd}")

        # Traverse tree until target node is found
        if current.value[cd] > value[cd]:
            print(f"111 Current ({current.value}) left was prev: {current.left.value}")
            current.left = self._delete(current.left, value, depth + 1)
            if current.left is not None:
                print(f"111 Current ({current.value}) left is now: {current.left.value}")
            else: 
                print(f"111 Current ({current.value}) left is now: {current.left}")
        elif current.value[cd] < value[cd]:
            print(f"118 Current ({current.value}) right was prev: {current.right.value}")
            current.right = self._delete(current.right, value, depth + 1)
            if current.right is not None:
                print(f"118 Current ({current.value}) right is now: {current.right.value}")
            else: 
                print(f"118 Current ({current.value}) right is now: {current.right}")
        else:
            print("Target node found")
            # Target node found
            if current.left is None and current.right is None:
                print("No children")
                return None
            # Only right child(ren)
            elif current.left is None:
                print(f"Returning right child: {current.right.value}")
                return current.right
            # Only left child(ren)
            elif current.right is None:
                print(f"Returning left child: {current.left.value}")
                return current.left
            # Has both left and right chidren
            else:
                print("2 children")
                axis = depth % self.k
                temp = self.find_min(current.right, axis, depth + 1)
                print(f"Minimum of right subtree: {temp.value}")
                print(f"Current ({current.value}) is now the min: {temp.value}")
                current.value = temp.value[:]
                print(f"145 Current ({current.value}) right was prev: {current.right.value}")
                current.right = self._delete(current.right, temp.value, depth + 1)
                if current.right is not None:
                    print(f"145 Current ({current.value}) right is now: {current.right.value}")
                else: 
                    print(f"145 Current ({current.value}) right is now: {current.right}")

        print("EXIT ===================================================")
        return current

    # Copied from ChatGPT
    def find_min(self, node, axis, depth):
        if node is None:
            return None
        
        cd = depth % self.k

        if cd == axis:
            if node.left is None:
                return node
            return self.find_min(node.left, axis, depth + 1)

        left_min = self.find_min(node.left, axis, depth + 1)
        right_min = self.find_min(node.right, axis, depth + 1)

        best = node
        for candidate in (left_min, right_min):
            if candidate and candidate.value[axis] < best.value[axis]:
                best = candidate
        return best

    def nearest(self):
        pass