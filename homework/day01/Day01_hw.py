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
## 讀入所需文件
'''

# %%
import pandas as pd
#TSV文件有別於CSV的文件是使用\ t作為分隔符，CSV則是使用，作為分隔符。
dataset = pd.read_csv(r'Restaurant_Reviews.tsv', sep='\t')

# %%
all_review = dataset['Review'].values
import pdb; pdb.set_trace()
# %%
'''
---
'''

# %%
'''
### 計算有多少個句子是以 . 結尾
'''

# %%
n=0
for wi in all_review:
    n += 1 if wi.endswith(".") else 0
print('There are {} sentences end with .'.format(n))

# %%
'''
### 將所有. 換成 ,
'''
# %%
# %%
print(f"[Before change]: {all_review[0]}")
all_review = [wi.replace(".", ",") for wi in all_review]
print(f"[Change . to ,]: {all_review[0]}")
# %%
'''
### 將所有sentence 中的第一個 the 置換成 The
'''

# %%
print(f"[Before change]: {all_review[2]}")
all_review = [wi.replace("the", "The", 1) for wi in all_review]
print(f"[Change 1st the to The]: {all_review[2]}")
# %%

# %%
'''
### 將偶數句子全部轉換為大寫，基數句子全部轉換為小寫
'''
# %%
print(f"[Before change at 1st elment]: {all_review[0]}")
print(f"[Before change at 2st elment]: {all_review[1]}")
for ii, wi in enumerate(all_review):
    if (ii+1) % 2 == 0:
        all_review[ii] = wi.lower() 
    else:
        all_review[ii] = wi.upper() 
print(f"[After change at 1st elment]: {all_review[0]}")
print(f"[After change at 2st elment]: {all_review[1]}")
# %%

# %%
'''
### 將所有句子合併在一起，並以' / ' 為間隔
'''
# %%
print(f"[Before change]: {all_review[:3]}")
all_review = ["".join((wi, "/")) for wi in all_review]
all_review = "".join(all_review)
print(f"[After change]: {all_review}")
