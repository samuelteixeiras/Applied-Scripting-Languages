# A00291713

from string import ascii_lowercase
text = input("Enter the text: ").lower()


frequencies = [0] * 26


for character in text:

    if character.isalpha():
        index = ascii_lowercase.find(character)
        frequencies[index] += 1


print("\n\nLetter Frequency")
for i in range(len(frequencies)):
    print(f"   {ascii_lowercase[i]}       {frequencies[i]}")


indexMostFrequent = frequencies.index(max(frequencies))

print(f"\nMost frequent letter: {ascii_lowercase[indexMostFrequent]}")