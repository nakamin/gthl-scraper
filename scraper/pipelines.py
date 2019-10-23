from google.cloud import firestore
from datetime import datetime
import scrapy


class FirestoreWriterPipeline(object):
    def open_spider(self, spider):
        db = firestore.Client()
        root = db.collection("snapshots")
        meta = root.document("meta")
        last_write = meta.get().get("last_update").date()
        now = datetime.now()
        self.should_run = last_write != now.date()
        if self.should_run:
            self.new_snapshot = root.document()
            self.new_snapshot.set({"timestamp": now})
            meta.set(
                {
                    "last_update": now,
                    "last_update_id": self.new_snapshot.get().id,
                }
            )

    def process_item(self, item, spider):
        if self.should_run:
            self.new_snapshot.collection("teams").document().set(dict(item))
        else:
            raise scrapy.exceptions.DropItem("Already pushed to firebase")
