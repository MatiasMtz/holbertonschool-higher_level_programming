#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the database
hbtn_0e_6_usa"""

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

    # Add a new record
    newState = State(name="Louisiana")
    session.add(newState)
    session.commit()

    # Print states.id after creation
    print("{}".format(newState.id))

    session.close()
