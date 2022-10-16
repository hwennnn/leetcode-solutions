class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = defaultdict(list)
        
        for path in paths:
            firstSpace = path.index(" ")
            directory, files = path[:firstSpace], path[firstSpace:].strip().split(" ")
            
            for file in files:
                fileName, content = file.split("(")
                content = content[:-1]
                
                contents[content].append(directory + "/" + fileName)
    
        return [content for content in contents.values() if len(content) > 1]