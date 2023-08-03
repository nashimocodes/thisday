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

    def cursor(self):
        """
        Returns the underlying session as a cursor.
        """

        return self._resource

    def _get_data_from_api(self, date: int, month: int):
        """
        Helper function to get data from the API
        """
        data = self._resource.get(
            f"https://byabbe.se/on-this-day/{month}/{date}/events.json"
        )

        print(data)
        return data

    def query(self, date: int, month: int):
        """
        Fetches and returns all the data of the events which happened on the given day
        """

        print("Querying the API")
