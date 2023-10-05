def get_odd_idx(list):
    idx = 1
    res = []
    while idx < len(list):
        res.append(list[idx])
        idx += 2
    return res

list = [1, 2, 3, 4, 5]
res = get_odd_idx(list)
print(res)