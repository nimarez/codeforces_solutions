def main():
    n = int(input())
    score_table, records = {}, []
    for _ in range(n):
        name, change = input().split(" "); change = int(change)
        score_table[name] = score_table.get(name, 0) + change
        records.append((name, score_table[name]))
    

    max_score = max(score_table.values())
    for name, score in records:
        if score_table[name] == max_score and score >= max_score:
            return name
   
if __name__ == "__main__":
    print(main())


# What we need is a data strucutre to look up all names with scores >= a number. So range queries
# HashTrees!