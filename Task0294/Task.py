k1, l1, m1 = map(int, input().split())
k2, l2, m2 = map(int, input().split())
count1 = k1 * (l1 / 100)
count2 = k2 * (l2 / 100)
result_k1 = k1 - count1
result_k2 = k2 - count2
bonus = abs(result_k1 - result_k2)
if result_k1 > result_k2:
    result = int(m1 * count1 + m2 * count2 + bonus * m1)
else:
    result = int(m1 * count1 + m2 * count2 + bonus * m2)
print(result)
