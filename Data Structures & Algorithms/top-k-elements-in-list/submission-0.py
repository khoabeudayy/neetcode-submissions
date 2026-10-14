class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for number in nums:
            if number not in count:
                count[number] = 1
            else:
                count[number] += 1

        pairs = list(count.items())
        sorted_pairs = sorted(pairs, key = lambda x: x[1])
        top_k = sorted_pairs[-k:]

        result = []

        for k in top_k:
            result.append(k[0])

        return result

        
        