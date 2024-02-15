#!/usr/bin/python3
"""
Module initializing BaseModel and FileStorage.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
