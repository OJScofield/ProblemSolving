class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        words_count = Counter(words)
        
        result = []
        
        for i in range(word_len):
            left = i
            right = i
            current_count = defaultdict(int)
            words_used = 0
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in words_count:
                    current_count[word] += 1
                    words_used += 1
                    
                    while current_count[word] > words_count[word]:
                        left_word = s[left:left + word_len]
                        left += word_len
                        current_count[left_word] -= 1
                        words_used -= 1
                    
                    if words_used == num_words:
                        result.append(left)
                        
                else:
                    current_count.clear()
                    words_used = 0
                    left = right
        
        return result
