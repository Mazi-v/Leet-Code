"""71. Simplify Path 
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        cleanPath = path.split("/")
        stack = []
        for i in range(len(cleanPath)):
            if  cleanPath[i]== "." or cleanPath[i]== "" :
                continue
            if cleanPath[i]!= "..":
                stack.append("/")
                stack.append(cleanPath[i])
            else: 
                if stack:
                    stack.pop(-1)
                    stack.pop(-1)
        return  "".join (stack)  if stack else "/"      
class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the input path into a list of cleaned path elements
        cleanPath = path.split("/")
        
        # Stack to keep track of valid path elements
        stack = []
        
        # Iterate through the cleaned path elements
        for i in range(len(cleanPath)):
            # Ignore current directory and empty elements
            if cleanPath[i] == "." or cleanPath[i] == "":
                continue
            
            # Handle valid directory names
            if cleanPath[i] != "..":
                stack.append("/")  # Add separator
                stack.append(cleanPath[i])
            else:
                # Handle ".." by popping the last valid directory
                if stack:
                    stack.pop(-1)
                    stack.pop(-1)
        
        # Join the stack elements to form the simplified path or return "/" if empty
        return "".join(stack) if stack else "/"