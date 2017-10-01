#!/bin/python3

import bisect


def compute_median(l, n):
    middle = n // 2
    if n % 2 != 0:
        return l[middle]
    return (l[middle] + l[middle - 1]) / 2


def activity_notifications():
    # skipping days < d
    sorted_expenditure = sorted(expenditure[:d])
    notifications = 0
    to_remove = 0
    for i in range(d, n):
        spent = expenditure[i]
        median = compute_median(sorted_expenditure, d)
        if spent >= 2 * median:
            notifications += 1

        # remove number out of scope
        
        del sorted_expenditure[bisect.bisect_left(sorted_expenditure, expenditure[to_remove])]
        to_remove += 1
        # insert sorted
        bisect.insort(sorted_expenditure, spent)
    return notifications


if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    expenditure = list(map(int, input().strip().split(' ')))
    # passing also n, to avoid computing len(expenditure)
    result = activity_notifications()
    print(result)
