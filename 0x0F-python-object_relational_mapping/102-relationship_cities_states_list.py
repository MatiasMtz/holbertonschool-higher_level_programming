#!/usr/bin/python3
"""script that lists all City objects from the database hbtn_0e_101_usa"""

if __name__ == "__main__":
    """Access to db and get the values"""
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    # Engine creation
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    # Session initializer (automatically commits and closes sessions)
    Session = sessionmaker(engine)
    session = Session()

# Obtaining Query Results
    query = session.query(State).join(City).order_by(City.id).all()
    for state in query:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
