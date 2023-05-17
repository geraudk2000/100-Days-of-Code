import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(df)

data_dict = {}
for (index, row) in df.iterrows():
    # print(row.letter, row.code)
    data_dict[row.letter] = row.code
print(data_dict)

data_dict2 = {row.letter: row.code for (index, row) in df.iterrows()}
# print(data_dict2)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    world = input("Please write you World. \n")
    # for letter in world:
    #     print(data_dict2[letter.upper()])

    try:
        world_nato = [data_dict2[letter.upper()] for letter in world]
    except KeyError:
        print("Only letter in th alphabet can be interpreted.")
        generate_phonetic()
    else:
        print(world_nato)


generate_phonetic()
