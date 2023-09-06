class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Split the path using / as the delimeter save to runner
        Create an empty list answer
        for index in runner:
            if the index is .. pop the last thing from answer if answer isn't empty
            if the index is "" or ".":
                continue
            keep adding to answer
        
        when the loop is done, create a string called result = "/"
        
        return result+'/'.join(answer)
            
        """
        answer = []
        
        for letter in path.split("/"):
            if letter == "..":
                if answer:
                    answer.pop()
            elif letter == "" or letter == ".":
                continue
            else:
                answer.append(letter)
        return "/"+ "/".join(answer)