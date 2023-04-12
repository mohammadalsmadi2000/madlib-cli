import re

def read_template(file_path):
    with open(file_path, "r") as file:
        template = file.read()
        return template

def parse_template(template):
    stripped_template = re.sub(r"\{(.*?)\}", "{}", template) # replace all instances of curly braces {} containing any characters with just a pair of empty curly braces {}.
    parts = re.findall(r"\{(.*?)\}", template) # searches for all occurrences of { and } characters in the template string
    return stripped_template,tuple(parts)
                                   

def get_user_inputs(parts):
    user_inputs = []
    for part in parts:
        user_input = input(f"Enter a/an {part}: ")
        user_inputs.append(user_input)
    return user_inputs

def merge(stripped_template, user_inputs):
    return stripped_template.format(*user_inputs)

def write_completed_madlib(completed_madlib):
    with open("completed_madlib.txt", "w") as file:
        file.write(completed_madlib)

def play_game():
    template = read_template("template.txt")# smaller.txt or template.txt
    stripped_template, parts = parse_template(template)
    user_inputs = get_user_inputs(parts)
    completed_madlib = merge(stripped_template, user_inputs)
    print(completed_madlib)
    write_completed_madlib(completed_madlib)
if __name__=="__main__":
    play_game() 
