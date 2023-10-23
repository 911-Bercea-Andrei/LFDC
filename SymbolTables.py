from HashTable import HashTable


class SymbolTable:
    def __init__(self, size):
        # we will be using 3 hash tables for integers, strings and identifiers
        self.int_hash_table = HashTable(size)
        self.str_hash_table = HashTable(size)
        self.identifier_hash_table = HashTable(size)

    def insert_integer(self, name, value):
        # insert int
        self.int_hash_table.insert(name, value)

    def insert_string(self, name, value):
        # insert str
        self.str_hash_table.insert(name, value)

    def insert_identifier(self, name, data):
        # insert identifier
        self.identifier_hash_table.insert(name, data)

    def get_integer(self, name):
        return self.int_hash_table.get(name)

    def get_string(self, name):
        return self.str_hash_table.get(name)

    def get_identifier(self, name):
        return self.identifier_hash_table.get(name)

    def delete_integer(self, name):
        return self.int_hash_table.delete(name)

    def delete_string(self, name):
        return self.str_hash_table.delete(name)

    def delete_identifier(self, name):
        return self.identifier_hash_table.delete(name)


symbol_table = SymbolTable(size=5)
symbol_table.insert_integer("number", 10)
symbol_table.insert_string("name", "Alice")
symbol_table.insert_identifier("x", {'type': 'string', 'value': "abc"})

print("Integer 'number':", symbol_table.get_integer("number"))
print("String 'name':", symbol_table.get_string("name"))
print("Identifier 'x':", symbol_table.get_identifier("x"))

symbol_table.delete_integer("number")
symbol_table.delete_string("name")
symbol_table.delete_identifier("x")