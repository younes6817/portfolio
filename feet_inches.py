def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(answer1, answer2):
    hesab = answer1 * 0.3048 + answer2 * 0.0254
    return hesab


# parsed = parse(feet_inches)
#
# result = convert(parsed['feet'], parsed['inches'])
#
# print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

