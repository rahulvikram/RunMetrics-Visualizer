"""These are helper functions designed to make the class code less cluttered."""

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
        o_inp = input("Type 'y' or 'n': ")
        if o_inp.lower() != 'y' and o_inp.lower() != 'n':
            raise Exception('Error')
        else:
            return o_inp
    except Exception:
        print("Error. Enter either 'y' or 'n'.")
        return override_input()
