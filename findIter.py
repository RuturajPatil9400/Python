import re
for match in re.finditer(r'\d+', 'There are 123 apples and 456 oranges'):
    print(match.group())  # Output: 123, 456