def reverse_string_by_words(s):
    # Split the string into words
    words = s.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed list of words back into a string
    reversed_string = ' '.join(reversed_words)
    return reversed_string

# Example usage
input_string = "how are you"
output_string = reverse_string_by_words(input_string)
print(output_string)  # Output: "you are how"
