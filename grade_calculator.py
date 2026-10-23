def get_scores():
    scores = []
    while True:
        entry = input("Enter a score (or 'done'): ").strip()
        if entry.lower() == "done":
            break
        scores.append(float(entry))
    return scores


def main():
    scores = get_scores()
    print("Scores entered:", scores)


if __name__ == "__main__":
    main()