"""This program prompts the user for the name and responds with a polite
 greeting.
"""


def main():
    """Prompt the user for their name and display a polite response."""
    name = input("Please enter your name: ")
    polite_response = "Hi " + name + ", let's explore some historical temperatures."
    print(polite_response)


if __name__ == "__main__":
    main()
