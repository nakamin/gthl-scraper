from google.cloud import firestore


class FirestoreWriterPipeline(object):
    def open_spider(self, spider):
        root = firestore.Client().collection("snapshots")
        self.new_doc = root.document()
        id = self.new_doc.get().id
        root.document("meta").set({"newest_id": id})
        self.teams_list = []

    def close_spider(self, spider):
        self.new_doc.set({"teams": self.teams_list})

    def process_item(self, item, spider):
        self.teams_list.append(dict(item))
