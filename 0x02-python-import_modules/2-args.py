#!/usr/bin/python3
import sys

number_of_arguments = len(sys.argv)
args_index = 1
if number_of_arguments == 1:
    print("0 arguments.")
else:
    if number_of_arguments == 2:
        print("1 argument:")
        print(f"1: {sys.argv[1]}")
    else:
        actual_args = len(range(1, number_of_arguments))
        print(f"{actual_args} arguments:")
        for i in range(1, number_of_arguments):
            print(f"{args_index}: {sys.argv[i]}")
            args_index += 1
