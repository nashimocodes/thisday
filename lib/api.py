import streamlit as st
import pandas as pd

from requests import Session
from streamlit.connections import ExperimentalBaseConnection

from lib.types import ThisDayData


class ThisDayAPIConnection(ExperimentalBaseConnection[Session]):
    def __init__(
        self, *args, connection_name: str = "somerandomconnectionname", **kwargs
    ) -> None:
        super().__init__(*args, connection_name=connection_name, **kwargs)
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

    def _get_data_from_api(self, date: int, month: int) -> ThisDayData:
        """
        Helper function to get data from the API
        """
        data = self._resource.get(
            f"https://byabbe.se/on-this-day/{month}/{date}/events.json"
        )

        formatted_data = ThisDayData.from_dict(data.json())
        return formatted_data

    def _convert_data_to_dataframe(self, data: ThisDayData) -> pd.DataFrame:
        """
        Converts the data to a pandas dataframe
        """

        for raw_data in data.events:
            d = list()
            for wikipedia in raw_data.wikipedia:
                d.append(f"[{wikipedia.title}]({wikipedia.wikipedia})")

            raw_data.wikipedia = " | ".join(d)

        return pd.DataFrame(data.events)

    def query(self, date: int, month: int):
        """
        Fetches and returns all the data of the events which happened on the given day
        """

        api_data = self._get_data_from_api(date, month)
        return self._convert_data_to_dataframe(api_data)
