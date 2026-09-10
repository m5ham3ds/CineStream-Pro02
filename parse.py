with open('app/src/main/java/com/example/ui/screens/player/ServerSelectionDialog.kt', 'r') as f:
    lines = f.readlines()

depth = 4
for i in range(264, 624):
    line = lines[i]
    for char in line:
        if char == '{': depth += 1
        elif char == '}': depth -= 1
    print(f"Line {i+1}: Depth {depth} - {line.strip()}")
