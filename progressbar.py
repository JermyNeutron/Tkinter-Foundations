# import math # for example

# def progress_bar(progress, total):
#     percent = 100 * (progress / float(total))
#     bar = '█' * int(percent) + '-' * int(100 - percent)
#     print(f"\r|{bar}| {percent:.2f}%", end="\r") # \r stays on same line instead of \n

# numbers = [x * 5 for x in range(2000, 5000)]
# results = []

# progress_bar(0, len(numbers))
# for i, x in enumerate(numbers):
#     results.append(math.factorial(x))
#     progress_bar(i + 1, len(numbers))

from tqdm import tqdm
from time import sleep
for i in tqdm(range(0,100), desc="Downloading SkyNet", unit_scale=2):
    sleep(.1)

    # unit_scale, position, unit

print('download complete\n\n')