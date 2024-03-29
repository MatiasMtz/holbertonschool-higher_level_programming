#!/usr/bin/python3
"""script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    """Access to db and get the values"""
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    # Engine creation
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    # Session initializer (automatically commits and closes sessions)
    Session = sessionmaker(engine)
    session = Session()

    # Obtaining Query Results
    for result in session.query(State).filter(State.name.contains("a")):
        print("{}: {}".format(result.id, result.name))

    session.close()
