data = {"apple": 3, "banana": 7, "orange": 5}

# maximum frequency value
max_freq = max(data.values())
print(max_freq)  # 7

# optional: key with maximum frequency
max_key = max(data, key=data.get)
print(max_key)   
