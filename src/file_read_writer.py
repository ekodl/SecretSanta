import csv


def load_participants():
    parts = []
    with open('inputs/participants', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            parts.append(row)

    return parts


def load_illegal_pairs():
    pairs = []
    with open('inputs/illegal_pairs', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            pairs.append([row[0], row[1]])
    return pairs


def save_matches(matches):
    with open('output.txt', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows([matches])