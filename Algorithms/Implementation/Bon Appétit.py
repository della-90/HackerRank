# Enter your code here. Read input from STDIN. Print output to STDOUT
n, k = map(int, raw_input().split())
prices = [int(x) for x in raw_input().split()]
bill = int(raw_input())

total = (sum(prices) - prices[k]) / 2

print "Bon Appetit" if bill == total else abs(total-bill)
