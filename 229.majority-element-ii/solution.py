class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majorities = [{"item": None, "cnt": 0}, {"item": None, "cnt": 0}, {"item": None, "cnt": 0}]
        for num in nums:
            hit = False
            for majority in majorities:
                if (majority["item"] == num):
                    majority["cnt"] += 1
                    hit = True
                    break

            if hit == False:
                hit = False
                for majority in majorities:
                    if (majority["cnt"] == 0):
                        majority["cnt"] = 1
                        majority["item"] = num
                        hit = True
                        break
                if hit == False:
                    for majority in majorities:
                        majority["cnt"] = max(majority["cnt"] - 1, 0)



        majorities[0]["cnt"] = 0
        majorities[1]["cnt"] = 0
        majorities[2]["cnt"] = 0
        for num in nums:
            for majority in majorities:
                if (majority["item"] == num):
                    majority["cnt"] += 1
                    break

        threshold = len(nums) / 3
        results = []
        for majority in majorities:
            if (majority["cnt"] > threshold):
                results.append(majority["item"])
        return results
