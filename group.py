from typing import List
def group_of_three (sublsts:List[int])->List[List[int]]:
    result = []
    for i in range(0,len(sublsts),3):
        result.append(sublsts[i:i+3])
    return result

example = [1,2,3,44,5,6,7,8,9,10]
groups = group_of_three(example)
print(groups)
