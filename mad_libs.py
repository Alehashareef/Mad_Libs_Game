def mad_libs():
    print("Welcome to Mad Libs! Fill in the blanks to create a funny story.\n")

    # Get user inputs
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")

    # The story
    story = f"One day, a {adjective} {animal} walked into {place}. \
It saw a {noun} and decided to {verb}. Everyone watching was amazed!"

    # Print the final mad lib
    print("\nHere is your Mad Libs story:\n")
    print(story)

# Run the Mad Libs game
mad_libs()
