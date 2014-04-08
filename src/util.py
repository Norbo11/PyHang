def get_choice(choices):
    choice = ""
    while (not choice in choices):
        choice = input()
    return choice
    
def format_points(points):
    return str(points) + " point" + ("s" if points > 1 else "")