def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

def count_words(lines):
    word_count = 0
    for line in lines:
        words = line.split()
        word_count += len(words)
    return word_count

def main():
    file_path = 'sample.txt'
    lines = read_file(file_path)
    
    if lines:
        print("Lines in file:")
        for line in lines:
            print(line)
        total_words = count_words(lines)
        print(f"\nTotal words: {total_words}")
    else:
        print("No content to display.")

if __name__ == "__main__":
    main()
