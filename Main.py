from Input_Padder import InputPadder

input_string = str(input("Enter the data: "))

padded_input_string = InputPadder(input_string).pad_input()

print("Padded Input String: ", padded_input_string)