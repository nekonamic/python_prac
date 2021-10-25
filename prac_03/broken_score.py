def judge_score(in_score):
    if in_score < 0:
        print("Invalid score")
    else:
        if in_score > 100:
            return "Invalid score"
        elif in_score > 90:
            return "Excellent"
        elif in_score > 50:
            return "Passable"
        else:
            return "Bad"


score = float(input("Enter score: "))
print(judge_score(score))
