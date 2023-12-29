"""These are helper functions designed to make the class code less cluttered."""
import time

# splits the output string into separate file and folder strings
def split_output(string):
    file_out = ''
    i = -1
    while string[i] != '/' and len(string) + i > 0:
        file_out = string[i] + file_out
        string = string[:-1]

    return file_out, string

# prompts user for override input
def override_input():
    try:
        o_inp = input("Type 'o' for overwrite or 'a' for append: ")
        if o_inp.lower() != 'o' and o_inp.lower() != 'a':
            raise Exception('Error')
        else:
            return o_inp
    except Exception:
        print("Error. Enter either 'o' or 'a'.")
        return override_input()
    
# wrapped timing code for reusability, returns a function's runtime
def time_function(func, *args, **kwargs):
    start = time.time()
    func(*args, **kwargs)
    end = time.time()
    elapsed = round(end-start, 6)
    return elapsed
