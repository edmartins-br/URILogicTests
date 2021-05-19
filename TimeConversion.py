sec = int(input())

h = sec // 3600
sec = (sec - (h * 3600))

m = sec // 60
sec = (sec - (m * 60))

s = sec

print("{}:{}:{}".format(h, m, s))