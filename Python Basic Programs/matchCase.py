grade = input("Enter your grade (A/B/C): ")

match grade:
    case "A"|"a":
        print("Excellent")
    case "B"|"b":
        print("Good")
    case "C"|"c":
        print("Average")
    case _:
        print("Fail")