def show(notes):

    print()

    print("Notebook")

    print()

    groups = {}

    for note in notes:

        groups.setdefault(

            note.category,

            []

        ).append(note)

    for category, items in groups.items():

        print(category)

        print()

        for note in items:

            print(

                "•",

                note.text

            )

        print()

    print(

        f"Total notes: {len(notes)}"

    )
