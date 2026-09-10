with open('app/src/main/java/com/example/ui/screens/player/ServerSelectionDialog.kt', 'r') as f:
    lines = f.readlines()

depth = 0
for i, line in enumerate(lines):
    for char in line:
        if char == '{': depth += 1
        elif char == '}': depth -= 1
    if i in [146, 166, 191, 263, 622, 623, 825, 854, 855, 856, 857, 858, 859, 860, 861]:
        print(f"L{i+1}: D{depth} | {line.strip()[:60]}")
