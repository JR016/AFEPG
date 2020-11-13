import FileManager, copy

stuff = FileManager.FileManager.FILE_N_CONTENT

def extra_string(key):
    """Returns a value depending of a key."""

    le_dict = {
        "css_reference" : "        <link rel=\"stylesheet\" href=\"style.css\"> \n\n",
        "js_reference"  : "        <script src=\"scriptsin.js\"></script> \n\n"}

    try:
        return le_dict[key]

    except KeyError:
        print(f"Sorry, but the option {key} is not defined.")

def main(): 

    html_css = copy.deepcopy(stuff["html"])
    title_index = find_that_string("        <title>Default Title</title> \n\n",html_css)
    body_index = find_that_string("    <body> \n",html_css)

    html_css.insert(title_index + 1, extra_string("css_reference"))
    html_css.insert(body_index + 2, extra_string("js_reference"))

    print_lines(html_css)
    
    
def print_lines(lst):
    """Prints elements in a list."""

    if isinstance(lst,list) or isinstance(lst,tuple):
        for line in lst:
            print(line)
    
def print_indexes_n_lines(lst):
    """Print indexes along with lines of a list."""

    if isinstance(lst,list) or isinstance(lst,tuple):
        for i, line in enumerate(lst,0):
            print(f"Index: {i}\nLine: {line}")


def find_that_string(string, lst):
    """Returns index of a string in a list."""

    if isinstance(lst,list) or isinstance(lst,tuple):

        if string not in lst:
            print(f"Sorry, but the string \"{string}\" is not present in the given list.")
            return None

        else:
            for i, line in enumerate(lst,0):
                if line == string:
                    return i


if __name__ == "__main__": 
    main()
