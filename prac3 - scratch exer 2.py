def main():
    score = float(input("Enter your score: "))
    while score < 0 or score > 100:
        print("Invalid score, please re-enter an appropriate value")
        score = float(input("Enter your score: "))
    if score < 50:
        print("This is a bad score")
    elif score > 50 and score < 90:
        print("This is a passable score")
    else:
        print("This is an excellent score")
    main()

main()