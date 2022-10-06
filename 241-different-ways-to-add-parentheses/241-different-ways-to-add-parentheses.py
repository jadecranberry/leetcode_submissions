class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result=[]
        if '+' not in expression and '-' not in expression and '*' not in expression:
            result.append(int(expression))
        else:
            for i in range(0, len(expression)):
                char=expression[i]
                if not char.isdigit():
                    leftParts = self.diffWaysToCompute(expression[0:i])
                    rightParts = self.diffWaysToCompute(expression[i+1:])
                    for part1 in leftParts:
                        for part2 in rightParts:
                            if char == '+':
                                result.append(part1+part2)
                            elif char == '-':
                                result.append(part1-part2)
                            elif char == '*':
                                result.append(part1*part2)
        return result                        
                