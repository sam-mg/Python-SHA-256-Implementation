from Input_Padder import InputPadder
from Padded_Parser import InputParser

input_string = str(input("Enter the data: "))

padded_input_string = InputPadder(input_string).pad_input()

print("Padded Input String: ", padded_input_string)

expanded_message_schedule = InputParser(padded_input_string).process_chunks()

print("Expanded Message Schedule: ", expanded_message_schedule)