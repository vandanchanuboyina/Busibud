def StringChallenge(input_str):
    max_unique_chars = 0

    for i in range(len(input_str)):
        for j in range(i + 1, len(input_str)):
            if input_str[i] == input_str[j]:
                substring = input_str[i + 1:j]
                unique_chars = len(set(substring))
                print(f"Matching pair: {input_str[i]}, Indexes: ({i}, {j}), Substring: {substring}, Unique characters: {unique_chars}")
                max_unique_chars = max(max_unique_chars, unique_chars)

    return max_unique_chars

# Example usage:
print(StringChallenge("ahyjakh"))  # Output: 4
