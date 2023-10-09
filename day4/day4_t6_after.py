if __name__ == '__main__':
    list = list(range(1000))
    idx = 0
    while idx < len(list):
        if list[idx] % 2 == 1:
            list.pop(idx)
        idx += 1
    print(list)