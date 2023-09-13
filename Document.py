

class MyDocument:
    def __init__(self, title: str, text: str, date: str, time: str, document_id: int):
        self.title = title
        self.text = text
        self.date = date
        self.time = time
        self.document_id = document_id

    def add_document_to_base(self, database: list) -> bool:
        #Check document in database
        for doc in database:
            if doc.title == self.title and doc.text == self.text:
                return False
        #Create doc for database

        database.append(self)
        return True

    @staticmethod
    def delete_document_from_base(self, id, database) -> bool:
        pass

    @staticmethod
    def get_lemm_inverse_frequency(self, lemm_id: int, result:float)-> bool:
        pass

    @staticmethod
    def get_lemm_inverse_frequency(self, lemm_str: str, result:float)-> bool:
        pass

    @staticmethod
    def get_word_weight_in_document(self, lemm_str: str, document_Id: int,result: float)-> bool:
        pass

    @staticmethod
    def get_lemm_weight_in_document(self, lemm_id: int, documentId:int, result: float)-> bool:
        pass

    @staticmethod
    def get_document_vector(self, document_Id)-> dict:
        pass
