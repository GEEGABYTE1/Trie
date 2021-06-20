# Trie 🌴

Trie Data Structure Re-creation within Python. 

Trie is essentially a data structure that has letters of each word as a node of a tree. We can search if a word is present in the tree by traversing letter by letter down the tree. If the path of the traverse is the same as the letters in the word, the word has been found, otherwise; it is not in the tree. 

This is data structure can be used to autocomplete text, text_search, prefix_matching, and much more. When it comes to working with strings, the trie data structure  is very effective and efficient ✅

# Implementation 📲

My implementation of the trie data structure is very simple. There is a list of words called `lst` in this case, and the trie will implement each word into a formation of a tree by adding each letter of the word to the tree. 

The Trie will add nodes to it's parent nodes as children in 3 cases:
  - 1) If there is a new letter 
  - 2) If there are the same back to back letters in a word.
  - 3) If the letter is the first letter in the trie
 
If the letter is similar to the current node value and is not right after the current node in the very word, the trie will skip the addition of the new node and move on. When the trie adds a new node, that new node becomes the current node and compares it to the new letter. If they are the same, the pattern repeats until we have completely added the word to the trie. 

Since we are adding each letter of  each word in a list, the time complexity of the `.implementation()` function is `O(N^2)`

# Search 🔎

The `.traverse()` function is very similar to the function that adds the nodes to the trie itself. The Trie will look at each child node of the corresponding parent. If one of the parent node's child matches with the current letter, it will add it to a "saved_path", and will make that child the current_node. This pattern will keep going until it reaches the leaf node. When the function is done traversing, it will compare the node values of the path to the actual word itself. If they are the same, it will return `True` or `False` otherwise.

The `.traverse()` function only compares each letter of the prompted word with the current_path, hence, giving at an `O(N)` time complexity. 

# More Information 📚

If you would like to try this version of the trie out, then run `implementation.py`

Users can also add their own words by adding another a list and changing the statement `test.implementation(lst)` with their desired list as an argument. Or they can modify `lst` itself with new elements. 

The underlying data structure of this Trie was both a tree and a list. The list was used to reference the upcoming nodes in a tree and to see if they were the same as the current nodes.

Made in Python 🐍






