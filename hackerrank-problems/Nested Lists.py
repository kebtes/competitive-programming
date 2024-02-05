if __name__ == '__main__':
    records = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        records.append([name, score])

    scores = set([record[1] for record in records])
    runner_up = sorted(scores)[1]

    output = [record[0] for record in records if record[1] == runner_up]
    output.sort()
    
    print("\n".join(output))