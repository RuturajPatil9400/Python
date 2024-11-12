import re
result = re.sub(r'foo', 'bar', 'foo and foo')
print(result)  # Output: bar and bar