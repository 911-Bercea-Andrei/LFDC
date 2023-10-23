from SymbolTables import SymbolTable

symbol_table = SymbolTable(size=100)

def scan(input_program):
    lines = input_program.split('\n')
    line_no = 0
    token_no = 0
    lexical_error = False

    for line in lines:
        line_no += 1
        tokens = line.split()

        for token in tokens:
            token_no += 1

            if token.isdigit():
                symbol_table.insert_integer(f"{line_no}:{token_no}", int(token))
            else:
                symbol_table.insert_string(f"{line_no}:{token_no}", token)

    return not lexical_error

if __name__ == "__main__":
    with open("p1.txt", "r") as file:
        input_program = file.read()

    no_lexical_errors = scan(input_program)

    if no_lexical_errors:
        print("lexically correct")
    else:
        print("lexical error")

    integer_value = symbol_table.get_integer("1:2")
    print("Value of 1:2 (integer symbol):", integer_value)

    string_value = symbol_table.get_string("2:3")
    print("Value of 2:3 (string symbol):", string_value)
