#!/usr/bin/python3
"""script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa"""

if __name__ == "__main__":
    """Access to db and get the values"""
    from model_state import Base, State
    from model_city import City
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
    newState = State(name="California")
    newCity = City(name="San Francisco")
    newState.cities.append(newCity)

    session.add(newState)
    session.add(newCity)
    session.commit()

    session.close()
