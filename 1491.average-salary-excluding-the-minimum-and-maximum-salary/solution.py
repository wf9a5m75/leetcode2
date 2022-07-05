class Solution:
    def average(self, salary: List[int]) -> float:
        minSalary = min(salary)
        maxSalary = max(salary)

        return (sum(salary) - minSalary - maxSalary) / (len(salary) - 2)
