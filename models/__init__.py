#add shbang python

# Path: models/__init__.py
# Compare this snippet from tests/test_models/test_engine/test_file_storage.py:
#         result = pep8s.check_files(['tests/test_models/test_engine/\
# test_file_storage.py'])
#         self.assertEqual(result.total_errors, 0,
#                          "Found code style errors (and warnings)."

from os import getenv

storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
#q:dont know why it doesnt work with db_storage import or models 

