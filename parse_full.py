with open('app/src/main/java/com/example/ui/screens/player/ServerSelectionDialog.kt', 'r') as f:
    lines = f.readlines()

depth = 0
for i, line in enumerate(lines):
    for char in line:
        if char == '{': depth += 1
        elif char == '}': depth -= 1
    if i >= 620:
        print(f"L{i+1}: D{depth} | {line.strip()[:60]}")
