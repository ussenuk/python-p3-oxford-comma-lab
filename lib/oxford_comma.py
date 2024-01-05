def oxford_comma(items):
    if len(items) == 1:
        return  ", ".join(items)
    elif len(items) < 3:
        items[-1] = "and " + items[-1]
        return  " ".join(items)
     
    items[-1] = "and " + items[-1]
    oxford_string = ", ".join(items)
    return oxford_string  
