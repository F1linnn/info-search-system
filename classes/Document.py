

class MyDocument:
    def __init__(self, title: str, path: str, text: str, date: str, time: str):
        self.title = title
        self.path = path
        self.text = text
        self.date = date
        self.time = time

    def add_document_to_base(self, database: list) -> bool:
        for doc in database:
            if doc.title == self.title and doc.text == self.text:
                return False


        database.append(self)
        return True
    def get_word_weight_in_document(self, termin: str)-> bool:
        return self.text.count(termin)


