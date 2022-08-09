
class NumberSort:
    
    def __init__(self):
        self.lowest_level = float('inf')
        self.highest_level = 0
        self.grid = [{} for _ in range(32)]
        
    #TODO handle dupes
        
    def set_lowest_level(self):
        for i in range(32):
            if self.grid[i]:
                self.lowest_level = i
                return
        
    def pop(self):
        num = 0
        mapp = self.grid[self.lowest_level]
        nodes = []
        while mapp:
            for i in range(10):
                if i in mapp:
                    num = num*10 + i
                    nodes.append((mapp, i))
                    mapp = mapp[i]
                    break
        for mapp, i in nodes[::-1]:
            if not mapp[i]:
                del mapp[i]
            
        self.set_lowest_level()
        return num
    
    def push(self, num):
        strnum = str(num)
        level = len(strnum) -1
        if level < self.lowest_level:
            self.lowest_level = level
        mapp = self.grid[level]
        for c in strnum:
            n = int(c)
            mapp[int(n)] = mapp.get(n, {})
            mapp = mapp[n]