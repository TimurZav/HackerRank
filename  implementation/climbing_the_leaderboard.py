

def insort_left(a: list, x: int, lo=0, hi=None) -> int:
    lo = bisect_left(a, x, lo, hi)
    a.insert(lo, x)
    return lo


def bisect_left(a: list, x: int, lo=0, hi=None) -> int:
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] > x: lo = mid+1
        else: hi = mid
    return lo


def climbingLeaderboard(ranked, player):
    ranked = list(dict.fromkeys(ranked))
    dict_ranked = {rank: index for index, rank in enumerate(ranked, start=1)}
    for score_player in player:
        index_player_to_dict = insort_left(ranked, score_player)
        dict_ranked[score_player] = index_player_to_dict + 1
        # del ranked[index_player_to_dict]

    return dict_ranked


if __name__ == '__main__':
    # ranked_count = int(input().strip())
    # ranked = list(map(int, input().rstrip().split()))
    # player_count = int(input().strip())
    # player = list(map(int, input().rstrip().split()))

    ranked_count = 7
    ranked = [100, 100, 50, 40, 40, 20, 10]
    player_count = 4
    player = [5, 25, 50, 120]

    dict_ranked = climbingLeaderboard(ranked, player)

    for score in player:
        print(dict_ranked[score])

