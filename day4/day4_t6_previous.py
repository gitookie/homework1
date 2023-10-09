if __name__ == '__main__':
    list = list(range(1000))
    for idx in range(len(list)):
        if list[idx] % 2 == 1:
            list.pop(idx)
    print(list)