print("Hello world")

numbers = [1,2,3,4,5]
total = 0

for number in numbers:
	total += number
print(total)

# Eğitici list comprehension
numbers_squared = [num**2 for num in numbers]
for i in numbers_squared:
    print(i)

print("Sağol mert hocam, fark ettim parantezleri müdahale ettik :D")