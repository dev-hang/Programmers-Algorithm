from itertools import combinations

def make_prime_number(nums):
    answer = 0
    
    def check_prime_num(num):
        for i in range(2, int(num**(1/2))+1):
            if num % i == 0:
                return False        
        return True
        
    for case in combinations(nums, 3):
        num = sum(case)
        if check_prime_num(num):
            answer += 1
        
    return answer



print(make_prime_number([1,2,3,4])) # result = 1
print(make_prime_number([1,2,7,6,4])) # result = 4