#Task 22

n = int(input("введите количество элементов первой последовательности:"))
m = int(input("введите количество элементов второй последовательности:"))
set_1 = set([int(input(f"введите {i+1} значение первого множества:")) for i in range(n)])
set_2 = set([int(input(f"введите {i+1} значение второго множества:")) for i in range(m)])
resalt = sorted(list(set_1.intersection(set_2)))
print("Уникальные элементы, встречающиеся в обоих множествах:")
for element in resalt:
    print(element)
    

# Task 24
n = int(input("введите количество кустов:"))
berries = list(map(int, input("введите количество ягод на кадом кусте через пробел:").split()))

max_harvest = 0

for i in range(n):
    harvest = berries[i] + berries[(i + 1) % n] + berries[(i - 1) % n]
    max_harvest = max(max_harvest, harvest)


print(max_harvest)


