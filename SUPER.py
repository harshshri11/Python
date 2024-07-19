class person:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class programmer(person):
    def __init__(self, name, id, lang):
        super().__init__( name, id)
        self.lang = lang

jay = person("jay",420)
print(jay.name,jay.id)
harsh = programmer("harsh", 1111, "python")
print(harsh.name, harsh.id, harsh.lang)
