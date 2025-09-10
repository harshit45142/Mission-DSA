from collections import Counter
def sherlockAndAnagrams(s):
    anagram_counts = Counter()
    n = len(s)
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            substring = s[i : i + length]
            sorted_substring = "".join(sorted(substring))
            anagram_counts[sorted_substring] += 1            
    total_anagram_pairs = 0
    for count in anagram_counts.values():
        total_anagram_pairs += (count * (count - 1)) // 2        
    return total_anagram_pairs
