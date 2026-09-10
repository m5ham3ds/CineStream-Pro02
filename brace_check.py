import sys

def check_braces(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    count = 0
    for i, line in enumerate(lines):
        if 'if (isLoading)' in line or 'if (isLoading && !isFailed)' in line or 'else if (isFailed)' in line:
            print(f"Line {i+1}: {line.strip()} (Depth: {count})")
        for char in line:
            if char == '{':
                count += 1
            elif char == '}':
                count -= 1
                
check_braces('app/src/main/java/com/example/ui/screens/player/ServerSelectionDialog.kt')
