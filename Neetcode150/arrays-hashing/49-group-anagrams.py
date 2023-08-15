class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            characters = [0] * 26
            for c in s:
                characters[ord(c) - ord('a')] += 1
            groups[tuple(characters)].append(s)

        return groups.values()
