class Solution:
    def celebrity(self, M):
        """ Brute Force - Use two arrays to store the number of people who know the celebrity and the number of people the celebrity knows.
            Then the celebrity will be the person who knows 0 people and is known by n-1 people.
            Time Complexity: O(n^2) + O(n) - Nested loops + for loop
            Space Complexity: O(n) - Two arrays
        
        IKnow = [0]*len(M)
        KnowMe = [0]*len(M)

        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1:
                    IKnow[i] += 1
                    KnowMe[j] += 1

        for celeb in range(len(M)):
            if IKnow[celeb] == 0 and KnowMe[celeb] == len(M) - 1:
                return celeb
        return -1
        """
        """ Better Approach - Use a stack to store the people and check if the person knows the other person.
            Time Complexity: O(n)
            Space Complexity: O(n)
            where n is the number of people
            because we are using a for loop to iterate through the matrix
            and we are using a return statement to return the result
            and we are using a return statement to return the result
        
        stack = []
        for i in range(len(M)):
            stack.append(i)
        while len(stack) > 1:
            i = stack.pop()
            j = stack.pop()
            if M[i][j] == 1:
                stack.append(j)
            else:
                stack.append(i)
        return stack.pop()
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        Extra stack space used, so interviewer not happy with the space complexity.
        """
        """ Optimal Solution - Use two pointers to find the celebrity. We use two pointers, one at the start and one at the end.
            We check if the person at the start knows the person at the end. If yes, then the person at the start cannot be the celebrity.
            If no, then the person at the end cannot be the celebrity.
            We do this until the two pointers meet.
            The person at the start or end is the celebrity.
            Time Complexity: O(n)
            Space Complexity: O(1)
        """
        top, bottom = 0, len(M) - 1
        while top < bottom:
            if M[top][bottom] == 1:
                top += 1
            elif M[bottom][top] == 1:
                bottom -= 1
            else:               # neither knows the other, so both cannot be the celebrity
                top += 1 
                bottom -= 1

        if top > bottom:
            return -1

        for i in range(len(M)):
            if i == top:
                continue
            if M[top][i] == 1 or M[i][top] == 0:
                return -1
        return top

M = [ [0, 1], [1, 0] ]
print(Solution().celebrity(M))