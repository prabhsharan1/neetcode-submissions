class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Using Hashmap firstly to sort the letter (a-z) such that
        eat = 1e, 1a, 1t and using that as key and for the value
        adding in the words with the same 1a,1e,1t
        ex {eat} : {tea, ate}
        Time Complexity : O(m * n) 
        m = length of the strs
        n = average length of the words in strs
        YT: https://youtu.be/vzdNOK2oB2E
        """
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 #Creates a list of 26 zeros a....z

            for c in s:
                count[ord(c) - ord("a")] += 1 # finds the position of c

            res[tuple(count)].append(s)
    
        return list(res.values())
