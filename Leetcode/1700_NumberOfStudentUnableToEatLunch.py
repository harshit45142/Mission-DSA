class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        squareStudents = students.count(0)
        roundStudents = students.count(1)

        for sandwich in sandwiches:
            if sandwich == 0: 
                if squareStudents > 0:
                    squareStudents -= 1
                else:
                    break 
            else: 
                if roundStudents > 0:
                    roundStudents -= 1
                else:
                    break

        return squareStudents + roundStudents
