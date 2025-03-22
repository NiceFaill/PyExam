from  itertools import product, permutations
from fnmatch import fnmatch

# stars = [""]
# for i in range(1, 5):
#     for x in product("0123456789", repeat=i):
#         stars.append("".join(x))

# for x in "0123456789":
#     for y in stars:
#         s = "1" + x + "2139" + y + "4"
#         if int(s) <= 10_000_000_000 and int(s) % 2023 == 0:
#             print(int(s), int(s) // 2023, sep="\t")
###################################################################
for n in range(1, 10_000_000_001, 2023):
    s = str(n)
    if fnmatch(s, "1?2139*4"):
        print(n, n // 2023)
        