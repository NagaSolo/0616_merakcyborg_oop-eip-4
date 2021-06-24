import json, os
class DB(object):

    """
        Here we defined our main class with an __init__ function.
        Whenever creating a Foobar Database we only need to pass the location of the database. 
        In the first __init__ function we take the location parameter and replace ~ or ~user with user’s home directory to make it work intended way. 
        And finally, put it in self.location variable to access it later on the same class functions. 
        In the end, we are calling the load function passing self.location as an argument.
    """
    def __init__(self, location):
        self.location = os.path.expanduser(location)
        self.load(self.location)

    """
        In the next load function we take the location of the database as a param. 
        Then check if the database exists or not. 
        If it exists, we load it with the _load() function (explained below). 
        Otherwise, we create an empty in-memory JSON object. 
        And finally, return true on success.
    """
    def load(self , location):
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}
        return True


    """
        In the _load function, we just simply open the database file from the location stored in self.location. 
        Then we transform it into a JSON object and load it into self.db variable.
    """
    def _load(self):
        self.db = json.load(open(self.location , "r"))

    """
        And finally, the dumpdb function: its name says what it does. 
        It takes the in-memory database (actually a JSON object) from the self.db variable and saves it in the database file! 
        It returns True if saved successfully, otherwise returns False.
    """
    def dumpdb(self):
        try:
            json.dump(self.db , open(self.location, "w+"))
            return True
        except:
            return False

    def set(self , key , value):
        try:
            self.db[str(key)] = value
            self.dumpdb()
            return True
        except Exception as e:
            print("[X] Error Saving Values to Database : " + str(e))
            return False

    """
        The set function is to add data to the database. 
        As our database is a simple key-value based database, we’ll only take a key and value as an argument.
        First, we’ll try to add the key and value to the database and then save the database. 
        If everything goes right it will return True. 
        Otherwise, it will print an error message and return False. 
        (We don’t want it to crash and erase our data every time an error occurs ?).
        get is a simple function, we take key as an argument and try to return the value linked to the key from the database. 
        Otherwise False is returned with a message.
    """
    def get(self , key):
        try:
            return self.db[key]
        except KeyError:
            print("No Value Can Be Found for " + str(key))  
            return False


    """
        delete function is to delete a key as well as its value from the database. 
        First, we make sure the key is present in the database. 
        If not we return False. 
        Otherwise, we delete the key with the built-in del which automatically deletes the value of the key. 
        Next, we save the database and it returns false.
    """
    def delete(self , key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dumpdb()
        return True

    """
        Here’s the function to reset the database, resetdb! 
        It's so simple: 
        first, what we do is re-assign our in-memory database with an empty JSON object and it just saves it! 
        And that's it! 
        Our Database is now again clean shaven.
    """
    def resetdb(self):
        self.db={}
        self.dumpdb()
        return True