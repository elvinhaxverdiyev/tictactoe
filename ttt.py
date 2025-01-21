def display(fields: list) -> None:
    sep_horizontal = "-----+-----+-----"
    sep_vertical = "     |     |"

    first = "  |  ".join(fields[:3])
    second = "  |  ".join(fields[3:6])
    third = "  |  ".join(fields[6:])

    print("\n")
    print(sep_vertical)
    print(f"  {first}  ")
    print(sep_horizontal)
    print(f"  {second}  ")
    print(sep_vertical)
    print(sep_horizontal)
    print(f"  {third}  ")
    print(sep_vertical)
    print("\n")
    
    
def check_winner(fields: list):
    combo = (
        #setir konbinasyalari
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        #sutun konbinasyalari
        (0, 3 ,6),
        (1, 4, 7),
        (2, 5, 8),
        #dioganal konbinasyalar
        (0, 4, 8),
        (2, 4, 6),
    )
    
    for winner in combo:
        a, b, c = winner
        if fields[a] == fields[b] == fields[c] != " ":
            return fields[a]
            
    if " " not in fields:
        return -1
    
    return None
    
    




