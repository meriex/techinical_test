def nth_most_rate_signature(lst, n):
    unique_list = list(set(lst))
    sorted_list = sorted(unique_list)
    ans = print(sorted_list[n - 1])
    return ans
nth_most_rate_signature([5, 4, 5, 4, 5, 4, 4, 5, 3, 3, 3, 2, 2, 1, 5], 2)
