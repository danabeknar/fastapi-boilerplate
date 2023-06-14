from datetime import datetime
from typing import Any

from bson.objectid import ObjectId
from pymongo.database import Database


class ShanyrakRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_shanyrak(self, user_id: str, data: dict):
        data["user_id"] = ObjectId(user_id)
        insert_result = self.database["shanyraks"].insert_one(data)
        return insert_result.inserted_id

    def get_shanyrak(self, id: str):
        shanyrak = self.database["shanyraks"].find_one(
            {
                "_id": ObjectId(id),
            }
        )
        return shanyrak

    def update_shanyrak(self, id: str, data: dict):
        filter = {
            "_id": ObjectId(id),
        }

        self.database["shanyraks"].update_one(filter, {"$set": data})

        shanyrak = self.database["shanyraks"].find_one(
            {
                "_id": ObjectId(id),
            }
        )

        return shanyrak

    def delete_shanyrak(self, id: str):
        filter = {
            "_id": ObjectId(id),
        }

        self.database["shanyraks"].delete_one(filter)
        return
