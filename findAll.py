import re
result = re.findall(r'\d+', 'There are 123 apples and 456 oranges')
print(result)  # Output: ['123', '456']