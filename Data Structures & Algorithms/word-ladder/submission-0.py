class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def find_match(word):
            found_words = []
            n = len(word)

            for i in range(n):
                for num in range(ord('a'), ord('z')+1):
                    new_word = word[:i] + chr(num) + word[i+1:]

                    if new_word != word and new_word in set_words:
                        found_words.append(new_word)
                        set_words.discard(new_word)
                
                if len(set_words) == 0: break
            return found_words

        if beginWord == endWord: return 1

        set_words = set(wordList)
        q = deque([beginWord])
        step = 0

        while q:
            step += 1
            for _ in range(len(q)):
                word = q.popleft()
                found_words = find_match(word)

                for w in found_words:
                    if w == endWord:
                        return step + 1
                    q.append(w)

        return 0

