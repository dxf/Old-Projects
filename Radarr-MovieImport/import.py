with open('movies.txt', 'r') as names:
    for line in names:
        open(f"{line.strip()}-480p.mp4", 'w').close()
