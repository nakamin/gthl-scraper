from google.cloud import firestore
from datetime import datetime
import scrapy


class FirestoreWriterPipeline(object):
    def open_spider(self, spider):
        self.db = firestore.Client()
        root = db.collection("standings-snapshots")
        meta = root.document("meta")
        last_write = meta.get("last_update").date()
        now = datetime.now()
        self.should_run = last_write != now.date()
        if self.should_run:
            new_snapshot = root.document()
            new_snapshot.set({"timestamp": now})
            last_update.set({'last_update': now})
            self.teams = new_snapshot.collection('teams')
            


    def process_item(self, item, spider):
        if self.should_run:
            self.teams.document().set(dict(item))
        else:
            raise scrapy.exceptions.DropItem("Already pushed to firebase")
