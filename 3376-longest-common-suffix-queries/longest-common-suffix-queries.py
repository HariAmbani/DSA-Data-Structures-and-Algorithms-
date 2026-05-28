class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_index = -1
        self.best_length = float('inf')


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        root = TrieNode()

        # Store globally smallest string index
        global_best_index = 0
        global_best_len = len(wordsContainer[0])

        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < global_best_len:
                global_best_len = len(wordsContainer[i])
                global_best_index = i

        # Build reversed trie
        for idx, word in enumerate(wordsContainer):
            rev = word[::-1]

            node = root

            # Update root best
            if (len(word) < node.best_length or
               (len(word) == node.best_length and idx < node.best_index)):
                node.best_length = len(word)
                node.best_index = idx

            for ch in rev:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                # Store shortest length word passing this node
                if (len(word) < node.best_length or
                   (len(word) == node.best_length and idx < node.best_index)):
                    node.best_length = len(word)
                    node.best_index = idx

        ans = []

        for query in wordsQuery:
            rev = query[::-1]
            node = root

            for ch in rev:
                if ch not in node.children:
                    break
                node = node.children[ch]

            ans.append(node.best_index)

        return ans