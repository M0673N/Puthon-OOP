def get_primes(nums):
    for num in nums:
        if num == 0 or num == 1:
            continue
        for i in range(2, num // 2 + 1):
            if (num % i) == 0:
                break
        else:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
