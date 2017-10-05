# PyArt by MohamadKh75
# 2017-10-05
# ********************

from pathlib import Path
import linecache


# Set the Alphabet folder path
alphabet_folder_path = Path("Alphabet").resolve()
number_folder_path = Path("Number").resolve()
result = open("Result.txt", 'w')


# Read all Letters
def letter_reader(user_text):

    for line_number in range(1, 10):

        arr = list(user_text)
        for x in range(0, len(arr)):
            letter = arr[x]

            # if it's Capital - AA is Capital A
            if 65 <= ord(letter) <= 90:
                letter_file = str(alphabet_folder_path) + str("\\") + str(letter) + str(letter) + ".txt"
                letter_txt = linecache.getline(letter_file, line_number).strip('\n')
                result.write(letter_txt)

            # if it's small - a is small a
            elif 97 <= ord(letter) <= 122:
                letter_file = str(alphabet_folder_path) + str("\\") + str(letter) + ".txt"
                letter_txt = linecache.getline(letter_file, line_number).strip('\n')
                result.write(letter_txt)

            # if it's Number
            elif 48 <= ord(letter) <= 57:
                letter_file = str(number_folder_path) + str("\\") + str(letter) + ".txt"
                letter_txt = linecache.getline(letter_file, line_number).strip('\n')
                result.write(letter_txt)

            # if it's Space
            elif ord(letter) == 32:
                result.write("   ")

            # if it's symbol - NOT SUPPORTED in Ver. 2.0 - Will Be Added in Ver. 3.0
            else:
                print("Sorry, Numbers and Symbols are NOT supported yet :)\n"
                      "I'll Add them in Ver. 2.0")
                return

        result.write('\n')

    result.close()
