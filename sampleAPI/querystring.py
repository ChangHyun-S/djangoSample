def select_usertable():
    query = """
        select * from usertable;
    """

    return query


def insert_usertable():
    query = """
        insert into usertable values (%(name)s);
    """

    return query
