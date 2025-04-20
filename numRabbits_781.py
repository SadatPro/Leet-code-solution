class Solution:
    def numRabbits(self, answers: List[int]) -> int:

     count = Counter(answers)

     total = 0

     for answer, freq in count.items():
        groupe_size = (answer + 1)
        groupe_count = math.ceil(freq/groupe_size)
        total += (groupe_size * groupe_count)

     return total
