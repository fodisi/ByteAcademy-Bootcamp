def intersection_count(lst1, lst2):
    return len(list(set(lst1) & set(lst2)))

def compute_divisors(num):
	return [x for x in range(1, num + 1) if num % x == 0]

def sum_of_divisors(num):
	return sum(compute_divisors(num))

def divisor_count(num):
	return len(compute_divisors(num))

def get_totatives(num):
    num_divisors = compute_divisors(num)
    return [x for x in range(1, num) if intersection_count(num_divisors, compute_divisors(x)) == 1]

def totient(num):
	return len(get_totatives(num))

print('type a number:')
num = int(input())
print('compute_divisors:')
print(compute_divisors(num))
print('sum_of_divisors:')
print(sum_of_divisors(num))
print('divisor_count:')
print(divisor_count(num))
print('get_totatives:')
print(get_totatives(num))
print('totient:')
print(totient(num))