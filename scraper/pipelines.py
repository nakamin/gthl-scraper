from google.cloud import firestore
from datetime import datetime
import scrapy


class FirestoreWriterPipeline(object):
    def open_spider(self, spider):
        root = firestore.Client().collection("snapshots")
        now = datetime.now()
        self.new_doc = root.document()
        self.new_doc.set({"timestamp": now})
        id = self.new_doc.get().id
        root.document("meta").set({"newest_id": id})
        self.teams_list = []

    def close_spider(self, spider):
        self.new_doc.set({"teams": self.teams_list})

    def process_item(self, item, spider):
        self.teams_list.append(dict(item))
