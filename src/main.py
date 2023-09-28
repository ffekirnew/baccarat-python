from cli import Cli

if __name__ == "__main__":
    print("How many hands do you want to simulate? ", end="")
    # validate and convert to int
    try:
        hands = int(input())
        cli = Cli(hands)
        cli.print_results()
    except ValueError:
        print("Invalid number of hands.")
        exit()
