class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        q = deque()
        q.append([startGene, 0])
        while q:
            start, count = q.popleft()
            print(start, count)
            j = 0
            while j < len(bank):
                geneMatch = 0
                gene = bank[j]
                for i in range(8):
                    if gene[i] != start[i]:
                        geneMatch += 1
                if geneMatch == 1:
                    if gene == endGene:
                        print(start, count, gene)
                        return count+1
                    q.append([bank.pop(j), count+1])
                    j-=1
                j+=1

        return -1
