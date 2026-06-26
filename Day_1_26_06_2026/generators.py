def even_num():
    for i in range(2,12,2):
        print(f"generated num :{i}")
        yield i

gen=even_num()
for val in gen:
    print(f"consumed num : {val}")
        



