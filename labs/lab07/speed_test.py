import time

data_list = list(range(1_000_000))
data_dict = {i: True for i in range(1_000_000)}
target = 999_999

start = time.time()
target in data_list
print(f"List: {time.time() - start:.5f}s")

start = time.time()
target in data_dict
print(f"Dict: {time.time() - start:.5f}s")