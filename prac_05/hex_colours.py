COLOR = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff", "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "Apricot": "#fbceb1", "Aqua": "#00ffff"}
for key, value in COLOR.items():
    print("{:<18} - {}".format(key, value))
color_name = input("Enter name of color: ")
while color_name != "":
    if color_name in COLOR.keys():
        print("{:<18} - {}".format(color_name, COLOR[color_name]))
    else:
        print("Invalid name of color")
    color_name = input("Enter name of color: ")
