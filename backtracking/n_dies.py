class Solution:
    def numRollsToTarget(self, n, k, target):
        
        faces = []
        
        def permute(arr):
            result = []
            if len(arr) == 1:
                return [arr[:]]


            for i in arr:
                n = arr.pop(0)
                perms = permute(arr)


                for perm in perms:
                    perm.append(n)
                result = result + perms
                arr.append(n)

            return result

        for i in range(n):
            for face in range(1,k+1):
                faces.append(face)
                
        
        print("jajajaj")
        print(permute(faces))
        
        
sol = Solution()
sol.numRollsToTarget(2, 6, 7)