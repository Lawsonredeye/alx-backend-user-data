#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.exc import NoResultFound

from user import Base
from user import User
from typing import Dict, Any


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Creates a new user into a database and commit all new entries.
        Returns
        ---
            User: User object
        """
        user_ = User(email=email, hashed_password=hashed_password)
        self._session.add(user_)
        self._session.commit()
        return user_

    def find_user_by(self, **kwargs: Dict[str, Any]) -> User:
        """Search db for arguments passed and returns a user object
        with the db data
        ------
        Returns
            user: User : instance which contains the searched data
        -------
        Raises
            NoResultFound: If args cant be found
            InvalidRequestError: if kwargs doesnt have any value
        ------
        """
        try:
            # session = self._session
            users = self._session.query(User).filter_by(**kwargs).one()
            return users
        except (InvalidRequestError, NoResultFound):
            raise

    def update_user(self, user_id: int, **kwargs: Dict[str, Any]) -> None:
        """Updates a user's attributes by user ID."""
        try:
            user = self.find_user_by(id=user_id)
            for key, value in kwargs.items():
                if key in ["email", "hashed_password", "session_id", "reset_token"]:
                    setattr(user, key, value)
            self._session.commit()
        except ValueError:
            raise
