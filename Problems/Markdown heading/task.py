def heading(a, b=1):
    if b > 5:
        return "###### " + a
    elif b < 2:
        return "# " + a
    else:
        return "#" * b + " " + a


# print(heading("A", 4))
