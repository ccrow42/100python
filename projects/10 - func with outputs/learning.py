def my_function():
    result = 3 * 2
    return result

output = my_function()

print (output)


###



def format_name(f_name, l_name):
    """
    Take a first and last name adn format it to return a titlecase version of the name.
    The return is a single string that has been concatinated
    """
    if f_name == "" or l_name == "":
        # return
        return "invalid inputs"
    return (f_name.title() + " " + l_name.title())

print(format_name("cHris", "crow"))

 
# docstrings

