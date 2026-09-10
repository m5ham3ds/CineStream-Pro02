with open('app/src/main/java/com/example/ui/screens/player/ServerSelectionDialog.kt', 'r') as f:
    lines = f.readlines()

depth = 3
for i in range(263, 624):
    line = lines[i]
    for char in line:
        if char == '{': depth += 1
        elif char == '}': depth -= 1
    print(f"L{i+1}: D{depth} | {line.strip()[:60]}")
