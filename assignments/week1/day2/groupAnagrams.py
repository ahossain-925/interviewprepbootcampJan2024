class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
    }
};
