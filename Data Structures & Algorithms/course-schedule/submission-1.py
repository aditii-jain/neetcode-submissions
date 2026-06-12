class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crs_pre = collections.defaultdict(list)

        for crs, pre in prerequisites:
            crs_pre[crs].append(pre) 
        
        visit = set()


        def dfs(crs):
            if crs in visit:
                return False
            if not crs_pre[crs]:
                return True
            
            visit.add(crs)
            for pre in crs_pre[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            crs_pre[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
        

            