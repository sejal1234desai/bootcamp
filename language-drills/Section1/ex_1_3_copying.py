#list_copying_pitfall

a = [1, 2, 3]
b = a  # Same reference
c = a[:]  # New copy

a.append(4)

print("a:", a)
print("b (same as a):", b)
print("c (copied):", c)
