import figures

def input_file(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

def convert_fig(str):
    words = str.split()
    try:
        match words[0].lower():
            case "square":
                return figures.Square(name=words[0], top_right=(int(words[2]), int(words[3])), side_length = int(words[5]))
            case "circle":
                return figures.Circle(name=words[0], center=(int(words[2]), int(words[3])), radius = int(words[5]))
            case "rectangle":
                return figures.Rectangle(name=words[0], top_right=(int(words[2]), int(words[3])), bottom_left=(int(words[5]), int(words[6])))
            case _:
                return "unknown figure!"
    except Exception as e:
        return "wrong syntax! write full figure name + needed params."


if __name__ == "__main__":
    mode = input("Write mode: f for file input, c for console input.    ")
    if mode=="f":
        filepath = input("input filepath. if empty, uses basic file info.txt:   ")
        print()
        strs = input_file("info.txt").split("\n") if not filepath else input_file(filepath).split("\n")
        for i in strs:
            print(convert_fig(i))
    elif mode=="c":
        strs = input("input figure details:  ").split("\n")
        for i in strs:
            print(convert_fig(i))
    else:
        print("wrong mode input")
    print()
    print(figures.Polygon(name='triangl', sides=3, points=[(5,5), (8, 8), (10, 2)]))
        