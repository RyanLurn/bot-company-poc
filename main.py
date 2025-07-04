def assess_expections():
    print("Assessing expectations...")


def assess_constraints():
    print("Assessing constraints...")


def assess_direction():
    print("Assessing direction...")


def assess_user():
    print("Assessing user...")
    assess_expections()
    assess_constraints()
    assess_direction()


def onboard():
    print("Onboarding...")
    assess_user()


def main():
    print("Welcome to bot company!")
    onboard()


if __name__ == "__main__":
    main()
