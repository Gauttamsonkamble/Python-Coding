
# gen = (x for x in range(6))

# print(gen)

# # print(next(gen))
# # print(next(gen))

# for value in gen:
#     print(value)

gen = (x for x in range(10) if x % 2 == 0)

for i in gen:
    print(i)