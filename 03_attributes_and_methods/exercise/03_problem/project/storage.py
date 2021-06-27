class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    @staticmethod
    def get_item_from_id(id_, collection):
        for item in collection:
            if item.id == id_:
                return item

    def edit_category(self, category_id, new_name):
        category = self.get_item_from_id(category_id, self.categories)
        category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.get_item_from_id(topic_id, self.topics)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = self.get_item_from_id(document_id, self.documents)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.get_item_from_id(category_id, self.categories)
        if category in self.categories:
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.get_item_from_id(topic_id, self.topics)
        if topic in self.topics:
            self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.get_item_from_id(document_id, self.documents)
        if document in self.documents:
            self.documents.remove(document)

    def get_document(self, document_id):
        document = self.get_item_from_id(document_id, self.documents)
        return document

    def __repr__(self):
        result = ""
        for document in self.documents:
            result += str(document) + "\n"
        return result
