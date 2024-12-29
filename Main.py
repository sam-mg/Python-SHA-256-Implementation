from Input_Padder import InputPadder
from Padded_Parser import InputParser
from Main_Class import MainClass

input_string = str(input("Enter the data: "))

padded_input_string = InputPadder(input_string).pad_input()

print("Padded Input String: ", padded_input_string)

expanded_message_schedule = InputParser(padded_input_string).process_chunks()

print("Expanded Message Schedule: ", expanded_message_schedule)

hash_result = MainClass(expanded_message_schedule).hash_message()

print("The Hash Result: ", hash_result)