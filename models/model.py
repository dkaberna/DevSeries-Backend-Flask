import json

class model:

    """
    A class that accessing a database
    ...

    Methods
    -------
    load_db(file_name)
        Loads json file based on input parameter.  Provides flexibility on JSON file.
    """

    # Load database based on input parameter filename
    def load_db(self, filename):
        with open(filename) as f:
            return json.load(f)