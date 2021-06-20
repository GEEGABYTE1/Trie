from tree import TreeNode

# Test inputs
lst = ['apple', 'ape', 'array', 'argon', 'advanced', 'Barry', 'Bee', 'Bat', 'Ball']


class Trie:

    def implementation(self, lst):
        tree = TreeNode(len(lst))
        head_node = tree
        letters_in_tree = []

        for word in lst:
            tree = head_node
            counter = 0
            for letter in word:
                if len(letters_in_tree) == 0:
                    tree.add_child(TreeNode(letter))
                    letters_in_tree.append(letter)
                
                elif word[0] == head_node.children[0].value and len(letters_in_tree) != 0 and counter == 0:
                    counter += 1
                    tree = tree.children[0]
                    letters_in_tree.append(word[0])
                    continue

                elif letter == letters_in_tree[-1]:
                    tree.add_child(TreeNode(letter))
                    letters_in_tree.append(letter)
                    tree = tree.children[0]
                    counter += 1
                    continue
                   
                else:
                    possible_letter = TreeNode(letter)
                    current_tree_lists = [i.value for i in tree.children]
                    if not letter in current_tree_lists:              
                        tree.add_child(possible_letter)
                        letters_in_tree.append(letter)
                
                if len(tree.children) == 2:
                    left_side = tree.children[0]
                    right_side = tree.children[-1]
                    if left_side.value == letter:
                        tree = left_side 
                        continue 
                    elif right_side.value == letter:
                        tree = right_side 
                        continue 
                else:
                    tree = tree.children[0]
                
                counter += 1
                
            






test = Trie()

test.implementation(lst)

