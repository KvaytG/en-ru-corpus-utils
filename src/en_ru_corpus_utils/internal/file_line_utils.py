
def count_lines(filePath: str) -> int:
    with open(filePath, 'r', encoding='utf-8') as file:
        return sum(1 for _ in file)
