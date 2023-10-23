def filledOrders(order, k):
    order.sort()
    sum = 0
    ans = 0
    for i in order:
        sum += i
        if sum <= k:
            ans += 1
        else:
            break

    return ans


# order = [5, 4, 6]
# k = 3

order = [10, 30]
k = 40
print(filledOrders(order, k))
