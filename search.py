class Search:

    def keyword(

        self,

        notes,

        text

    ):

        return [

            note

            for note in notes

            if text.lower()

            in note.text.lower()

            or text.lower()

            in note.title.lower()

        ]
