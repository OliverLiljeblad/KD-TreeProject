# KD-TREE PROJECT
# Authors: Micki Eustache :/
# Debugged with ChatGPT
import math

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
    
    def delete(self, value):
        self.root = self._delete(self.root, value, 0)
        self.count -= 1
    
    def _delete(self, node, value, depth):
        # Return none if node not found        
        if not node:
            return None

        cd = depth % self.k

        # Traverse tree until target node is found
        if node.value[cd] > value[cd]:
            node.left = self._delete(node.left, value, depth + 1)
        elif node.value[cd] < value[cd]:
            node.right = self._delete(node.right, value, depth + 1)
        else:
            # Target node found
            # Is a leaf node
            if node.left is None and node.right is None:
                return None
            # Only right child(ren)
            elif node.left is None:
                return node.right
            # Only left child(ren)
            elif node.right is None:
                return node.left
            # Has both left and right chidren
            else:
                dim = depth % self.k
                temp = self.find_min(node.right, dim, depth + 1)
                node.value = temp.value[:]
                node.right = self._delete(node.right, temp.value, depth + 1)

        return node

    # Referenced from https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/kdtrees.pdf
    def find_min(self, node, dim, depth):        
        if node == None:
            return None
        
        cd = depth % self.k

        if cd == dim:
            if node.left is None:
                return node
            return self.find_min(node.left, dim, depth + 1)
            
        left_min = self.find_min(node.left, dim, depth + 1)
        right_min = self.find_min(node.right, dim, depth + 1)
        
        minimum = node

        if left_min and left_min.value[dim] < minimum.value[dim]:
            minimum = left_min
        if right_min and right_min.value[dim] < minimum.value[dim]:
            minimum = right_min
        
        return minimum

    def nearest(self, value):
        # Raise error for invalid inputs
        if len(value) != self.k:
            raise IndexError("Input does not meet dimension requiremnt")
        best_point, best_dist = self._search(self.root, value, 0, self.root, self.distance(self.root.value, value))
        return best_point, best_dist

    def _search(self, node, value, depth, best_point, best_dist):
        if node == None:
            return best_point, best_dist

        current_dist = self.distance(value, node.value)
        if current_dist < best_dist:
            best_dist = current_dist
            best_point = node
        
        cd = depth % self.k

        if value[cd] < node.value[cd]:
            near = node.left
            far = node.right
        else:
            near = node.right
            far = node.left
        
        best_point, best_dist = self._search(near, value, depth + 1, best_point, best_dist)
        
        plane_dist = abs(value[cd] - node.value[cd])
        if plane_dist < best_dist:
            best_point, best_dist = self._search(far, value, depth + 1, best_point, best_dist)

        return best_point, best_dist

    def distance(self, value1, value2):
        # Calculate euclidian distance        
        dist = 0

        for i in range(self.k):
            dist += (value1[i] - value2[i])**2

        return math.sqrt(dist)