class Service:
    _name = "unknown"
    _version = "0.0.0.0"
    _comment = "unknown"
    

    #Create new service
    def __init__(self, name, version, comment="unknown"):
        self._name = name
        self._version = version
        self._comment = comment

    #Print out contents of the class
    def dump(self):
        print(self._name, self._version, self._comment, sep=" | ")

    #Print out name attribute
    def name_match(self, name):
        return self._name == name
    
    #Print out name attribute
    def name(self):
        return self._name

    #Print out version attribute
    def version(self):
        return self._version

    #Print out version attribute
    def set_version(self, version):
        self._version = version

    #Print out version attribute
    def comment(self):
        return self._comment

    def set_comment(self, comment):
        self._comment = comment
