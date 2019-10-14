# re库的贪婪匹配和最小匹配

import re
match1 = re.search(r'PY.*N', 'PYANBNCNDN')   # 贪婪匹配
print(match1.group(0))

match1 = re.search(r'PY.*?N', 'PYANBNCNDN')  # 最小匹配
print(match1.group(0))
