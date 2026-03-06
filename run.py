from src.frequency_counter import char_frequency, format_output

if __name__ == "__main__":
    text = input("Enter a string: ")

    freq = char_frequency(text)

    print(format_output(freq))