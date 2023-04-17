def read_input():
  # This function should read input from both keyboard and file
    # Use uppercase i (keyboard input) and uppercase f (file input),
    # to select the type of input to follow.
    input_type = input().rstrip()
    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'F':
        with open('tests/06', 'r') as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()

   # Example return value, note the rstrip function
    return pattern, text

def print_occurrences(output):
    # This function should control the output, no return value is required
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
  # This function should find occurrences using the Rabin-Karp algorithm
    pattern_length = len(pattern)
    text_length = len(text)
    pattern_hash = hash(pattern)
    text_hash = hash(text[:pattern_length])
    occurrences = []

    for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash and pattern == text[i:i+pattern_length]:
            occurrences.append(i)

        if i < text_length - pattern_length:
            text_hash = hash(text[i+1:i+pattern_length+1])

  # And return the variable to be enumerated
    return occurrences


# This part starts the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
