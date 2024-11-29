class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total=0
        prev=-2
        for i in range(len(flowerbed)):
            if flowerbed[i]:
                total+=(i-prev-2)//2
                prev=i
        total+=(len(flowerbed)-prev-1)//2
        return total>=n