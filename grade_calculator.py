def get_scores():
    scores = []
    while True:
        entry = input("Enter a score (or 'done'): ").strip()
        if entry.lower() == "done":
            break
        try:
            score = float(entry)
        except ValueError:
            print("Please enter a number.")
            continue
        if not 0 <= score <= 100:
            print("Score must be between 0 and 100.")
            continue
        scores.append(score)
        
    return scores
def compute_average(scores):
    return sum(scores) / len(scores)

def main():
    scores = get_scores()
    if not scores:
        print("No scores entered.")
        return
    average = compute_average(scores)
    print(f"Average: {average:.2f}")


if __name__ == "__main__":
    main()