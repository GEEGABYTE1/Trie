from tree import TreeNode

# Test inputs
lst = ['apple', 'ape', 'array', 'argon', 'advanced', 'Barry', 'Bee', 'Bat', 'Ball']


class Trie:

    def implementation(self, lst):
        self.tree = TreeNode(len(lst))
        head_node = self.tree
        letters_in_tree = []

        for word in lst:
            word = word.lower()
            self.tree = head_node
            counter = 0
            for letter in word:
                if len(letters_in_tree) == 0:
                    self.tree.add_child(TreeNode(letter))
                    letters_in_tree.append(letter)
                
                elif word[0] == head_node.children[0].value and len(letters_in_tree) != 0 and counter == 0:
                    counter += 1
                    self.tree = self.tree.children[0]
                    letters_in_tree.append(word[0])
                    continue

                elif letter == letters_in_tree[-1]:
                    self.tree.add_child(TreeNode(letter))
                    letters_in_tree.append(letter)
                    self.tree = self.tree.children[0]
                    counter += 1
                    continue
                   
                else:
                    possible_letter = TreeNode(letter)
                    current_tree_lists = [i.value for i in self.tree.children]
                    if not letter in current_tree_lists:              
                        self.tree.add_child(possible_letter)
                        letters_in_tree.append(letter)
                
                if len(self.tree.children) == 2:
                    left_side = self.tree.children[0]
                    right_side = self.tree.children[-1]
                    if left_side.value == letter:
                        self.tree = left_side 
                        continue 
                    elif right_side.value == letter:
                        self.tree = right_side 
                        continue 
                else:
                    self.tree = self.tree.children[0]
                
                counter += 1
        
        self.tree = head_node


    def traverse(self):
        user_prompt = input("Please enter a word you are trying to find in a trie: ")
        tree = self.tree

        user_prompt = user_prompt.lower()
        user_letters = [i for i in user_prompt]

        returned_path = []

        nodes = [self.tree]
        while len(nodes) > 0 and len(user_letters) > 0:
            current_node = nodes.pop()
            if current_node.value == user_letters[0]:
                returned_path.append(current_node)
                user_letters.pop(0)
            nodes += current_node.children
        

        returned_path = [i.value for i in returned_path]
        user_letters  = [i for i in user_prompt]
        if returned_path == user_letters:
            return True 
        else:
            return False
        
        
            



        


    
                
            






test = Trie()

test.implementation(lst)
print(test.traverse())


