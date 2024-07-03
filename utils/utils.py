def get_all_subclasses(cls):
    all_subclasses = []
    all_name = []
    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))
    for subclass in all_subclasses:
        all_name.append(subclass.__tablename__)
    return all_name
