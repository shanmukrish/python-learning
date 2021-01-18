def create_tuples():
    return ('shammu','yogu','testing')

def is_present(element):
    return element in create_tuples()

def find(element):
    return create_tuples().find(element) 

def count(element):
    return create_tuples().count(element)


