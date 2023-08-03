import requests

from requests import Session
from streamlit.connections import ExperimentalBaseConnection

class ThisDayAPIConnection(ExperimentalBaseConnection[Session]):
    def __init__(self, connection_name: str, **kwargs) -> None:
        super().__init__(self, connection_name, **kwargs)
        self._resource = self._connect()

    def _connect(self) -> Session:
        """
        Create and return a new session connection.
        """
        return Session()
