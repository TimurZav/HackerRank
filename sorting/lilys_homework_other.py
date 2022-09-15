def count_swaps(sorted_list, num_list):
    swaps = 0
    position_map = {num: index for index, num in enumerate(num_list)}
    for index, num in enumerate(num_list):
        if num != sorted_list[index]:
            swaps += 1
            pos = position_map[sorted_list[index]]
            # IMPORTANT: update indices within position_map
            position_map[num_list[index]] = pos
            position_map[num_list[pos]] = index
            # swap values as well
            num_list[index], num_list[pos] = num_list[pos], num_list[index]

    return swaps


def lilysHomework(arr):
    arr_copy = list(arr)

    sorted_list_asc = sorted(arr, reverse=False)
    sorted_list_dsc = sorted(arr_copy, reverse=True)

    swaps_a = count_swaps(sorted_list_asc, arr)
    swaps_d = count_swaps(sorted_list_dsc, arr_copy)

    return min(swaps_a, swaps_d)


if __name__ == "__main__":
    # n = int(input().strip())
    # arr = list(map(int, input().strip().split(' ')))
    n = 5
    arr = [3, 4, 2, 5, 1]
    result = lilysHomework(arr)
    print(result)
