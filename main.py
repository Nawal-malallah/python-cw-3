# write your code here
favAni = ["dog" , "cat" , "monkey" , "rabbit"]
print(favAni)
print(favAni[1])
favAni.remove("monkey")
favAni.append("fish")

for n in favAni:
    print(f"I love {n}")

numbers = [1 , 2 , 3 , 4 , 5]
numbers_sum = 0

for num in numbers:
    numbers_sum += num

print(numbers_sum)