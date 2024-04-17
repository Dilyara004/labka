def remove_spaces(input_str):
    return input_str.replace(" ", "")

def to_lower_case(input_str):
    return input_str.lower()

def compose(*functions):
    def inner(input_str):
        result = input_str
        for func in functions:
            result = func(result)
        return result
    return inner

composed_function = compose(remove_spaces, to_lower_case)

# Пример использования
input_string = " Shaimerden Dilyara "
output_string = composed_function(input_string)
print(output_string)
