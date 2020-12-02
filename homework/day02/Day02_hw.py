# %%
'''
# 作業目標：運用課程所學，操作字串達到預期輸出
'''

# %%
'''
---
'''

# %%
'''
### isnumeric(), isdigit(), isdecimal() 各有幾個
'''

# %%
test_string = ['5.9', '30', '½', '³', '⑬']
isnumeric_count = 0
isdigit_count = 0
isdecimal_count = 0
# %%
def spam(s, isnumeric_count, isdigit_count, isdecimal_count):
    isnumeric_count += 1 if s.isnumeric() else 0
    isdigit_count   += 1 if s.isdigit() else 0
    isdecimal_count += 1 if s.isdecimal() else 0
    return isnumeric_count, isdigit_count, isdecimal_count
#    for attr in ['isnumeric', 'isdecimal', 'isdigit']:

for ts in test_string:
    isnumeric_count, isdigit_count, isdecimal_count = spam(ts, isnumeric_count, isdigit_count, isdecimal_count)
# %%
print('isnumeric_count: {}'.format(isnumeric_count))
print('isdigit_count: {}'.format(isdigit_count))
print('isdecimal_count: {}'.format(isdecimal_count))

# %%
'''
---
'''

# %%
'''
## 運用formatting 技巧 output
    * Accuracy: 98.13%, Recall: 94.88%, Precision: 96.29%
'''

# %%
accuracy = 98.129393
recall =   94.879583
precision =96.294821

# %%
import pdb; pdb.set_trace()
print(f"accuracy:\t{accuracy:.2f}%")
print(f"recall:\t\t{recall:.2f}%")
print(f"precision:\t{precision:.2f}%")

# %%
accuracy = 0.98129393
recall =   0.94879583
precision =0.96294821

# %%
print(f"accuracy:\t{accuracy:.2%}")
print(f"recall:\t\t{recall:.2%}")
print(f"precision:\t{precision:.2%}")

# %%
'''
---
'''

# %%
'''
## 依照只是轉換number output format
'''

# %%
number = 3.1415926

# %%
'''
#### 轉換為科學符號表示法 (小數點後兩位)
'''

# %%
print(f"number = {number:.2E}")

# %%
'''
#### 轉換為%
'''

# %%
print(f"number = {number:%}")

# %%
'''
#### 補零成為3.14159300
'''

# %%
print(f"{number:0<10f}")
