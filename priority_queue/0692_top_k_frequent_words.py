import heapq

class Solution:
    def topKFrequent(self, words: list, k: int) -> list:
        word_to_entry = {}
        priority_q = []

        for word in words:
            if word not in word_to_entry:
                # heapq implements a min heap.
                # Keep track of the negative frequency to get the most k frequent words
                word_to_entry[word] = [-1, word]
                priority_q.append(word_to_entry[word])
            else:
                word_to_entry[word][0] -= 1

        heapq.heapify(priority_q)
        top_k = []

        for _ in range(k):
            top_k.append(heapq.heappop(priority_q)[1])

        return top_k
        
        
if __name__ == "__main__":
    test = ['aaa', 'aa', 'a']
    solu = Solution()
    solu.topKFrequent(test, 1)