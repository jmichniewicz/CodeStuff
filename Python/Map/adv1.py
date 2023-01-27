def lines_to_elves(lines):
    snacks = []
    for line in lines:
        stripped_line = line.strip()
        
        if stripped_line == "":
            yield snacks == []
        else:
            snacks.append(int(stripped_line))
            
with open("input.txt", "r") as file:
    elves = lines_to_elves(file)
    total_snacks_per_elf = list(map(sum, elves))