#KD-TREE PROJECT
#Authors: Micki Eustache
# delete, _delete, copy_point, and find_min copied from https://www.geeksforgeeks.org/dsa/deletion-in-k-dimensional-tree/

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
        pass
    
    def delete(self, value):
        self.count -= 1
        return self._delete(self.root, value, 0)
    
    def _delete(self, current, value, depth):
        # Return none if node not found
        if not current:
            return None
        
        cd = depth % self.k

        # Traverse tree until target node is found
        if current.value[cd] > value[cd]:
            current.left = self._delete(current.left, value, depth + 1)
        elif current.value[cd] < value[cd]:
            current.right = self._delete(current.right, value, depth + 1)
        else:
            # Target node found
            # Only right child(ren)
            if current.left is None:
                return current.right
            # Only left child(ren)
            elif current.right is None:
                return current.left
            # Has both left and right chidren
            else:
                temp = self.find_min(current.right, depth + 1)
                current.value = temp.value
                current.right = self._delete(current.right, temp.value, depth + 1)

        return current

    def find_min(self, root, d):
        pass

    def nearest(self):
        pass

    def copy_point(self, point1, point2):
        for i in range(self.k):
            point1[i] = point2[i]