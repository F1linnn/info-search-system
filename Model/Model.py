import math
class Model:
    def __init__(self):
        self.__documents = []
        self.__IDF = {}
        self.__results_similar = {}
        self.__TF_IDF = []
        self.__TFs = []
        self.__docs_vectors = []
        self.__query_vector = []
        self.__dictionary = []

    def set_result_similar(self, result):
        self.__results_similar = result

    def get_irrelevant_documents(self):
        filtered_dict = {key: value for key, value in self.__results_similar.items() if value == 0}
        return filtered_dict

    def get_relevant_documents(self):
        filtered_dict = {key: value for key, value in self.__results_similar.items() if value > 0.049}
        return filtered_dict

    def get_bad_relevant_documents(self):
        filtered_dict = {key: value for key, value in self.__results_similar.items() if  0.05 >= value > 0}
        return filtered_dict

    def get_result_similar(self):
        filtered_dict = {key: value for key, value in self.__results_similar.items() if value != 0}
        return filtered_dict

    def set_docs_vectors(self, matrix):
        self.__docs_vectors = matrix

    def get_docs_vectors(self):
        return self.__docs_vectors

    def set_dictionary(self, dictionary):
        self.__dictionary = dictionary

    def get_dictionary(self):
        return self.__dictionary

    def set_query_vector(self,vector):
        self.__query_vector = vector

    def get_query_vector(self):
        return self.__query_vector

    def clear_query_vector(self):
        self.__query_vector = []

    def set_TFs(self,TFs):
        self.__TFs = TFs

    def get_TFs(self):
        return self.__TFs

    def set_documents(self, documents):
        self.__documents = documents

    def get_documents(self):
        return self.__documents

    def get_document_by_id(self, id: int):
        return self.__documents[id]

    def set_IDFS(self, IDFS):
        self.__IDF = IDFS

    def get_IDFS(self):
        return self.__IDF

    def set_TF_IDF(self, TF_IDF):
        self.__TF_IDF = TF_IDF

    def get_TF_IDF(self):
        return self.__TF_IDF

    #Getting only termins without IDFS value.
    def get_termins(self):
        return [key for key in self.__IDF]
