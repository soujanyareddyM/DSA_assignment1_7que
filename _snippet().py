def brackets_are_balanced(code):
    stack = []
    opening_brackets = set(['(', '[', '{'])
    closing_brackets = set([')', ']', '}'])
    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for char in code:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            if bracket_pairs[char] != stack.pop():
                return False
    return not stack

# Example 
code_snippet = "(x + y) * (z - w)"
result = brackets_are_balanced(code_snippet)
print(result)

code_snippet = "{ a + [ b + ( c + d ) ] + e } / 2"
result = brackets_are_balanced(code_snippet)
print(result)  

code_snippet = "if (x > y] { z = x - y; }"
result = brackets_are_balanced(code_snippet)
print(result)  