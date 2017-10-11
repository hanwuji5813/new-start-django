h = []
a = [1, 2, 3, 4, 5, 6]
b = [6, 5, 4, 3, 2, 1]
c = {"x": 1, "y": 2, "z": 3}
d = dict(zip(c.values(), c.keys()))
e = list(enumerate(c))
f = "Everything is ok? Everything is good ha."
g = f.split(" ")
for i, string in enumerate(g):
    if "Everything" in string:
        g[i] = "Python"
x = " ".join(g)
print(x)