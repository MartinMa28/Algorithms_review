class Solution:
    def groupAnagrams(self, strs: list) -> list:
        chs_to_words = {}

        for s in strs:
            sorted_str = str(sorted(s))
            bucket = chs_to_words.get(sorted_str, [])
            bucket.append(s)
            chs_to_words[sorted_str] = bucket

        return chs_to_words.values()
        