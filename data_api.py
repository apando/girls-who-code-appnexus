from contextlib import contextmanager
import datetime
from random import randint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models

class _DataLayer():
    def __init__(self):
        pass

    @contextmanager
    def session(self):
        """
        Create a session to interact with a local sqlite database
        :return:
        """
        _Session = sessionmaker(bind=create_engine("sqlite:///perf.db",
                                                   pool_recycle=3600,
                                                   echo=True),
                                expire_on_commit=False)
        _session = _Session()
        try:
            yield _session
            _session.commit()
        except:
            _session.rollback()
            raise
        finally:
            _session.close()

class CoolAPI():
    """
    Provides helper functions to create, fetch, and insert data into the database.
    """
    def __init__(self, initialize=False):
        if initialize:
            self._initialize_data()

        self._data = _DataLayer()

    def _clear_data(self):
        """
        Remove all existing tables and data to start fresh
        :return:
        """
        with self._data.session() as session:
            # Clear everything!
            models.Base.metadata.drop_all(bind=session.bind)

    def _initialize_data(self):
        """
        Create fake data and insert it into the database.
        :return:
        """
        self._clear_data()
        with self._data.session() as session:
            # Create tables
            models.Base.metadata.create_all(bind=session.bind)

            #todo add another campaign
            creative_ids = [100, 101, 102, 103, 104, 105]
            performance_data = []

            # Insert randomly generated hourly data for 30 days
            for ymdh in [datetime.datetime(2014, 7, 1, 0, 0, 0) + \
                               datetime.timedelta(hours=x) for x in range(0, 720)]:
                for creative in creative_ids:
                    performance_data.append(
                        models.PerformanceData(ymdh=ymdh,
                                               campaign_id=100,
                                               creative_id=creative,
                                               imps=randint(0,5000),
                                               clicks=randint(0,20))
                    )
            session.add_all(performance_data)

    def get_campaign_data(self, start, end):
        """
        Fetch records from table performance_data
        :param start: datetime.datetime start time for desired records
        :param end: datetime.datetime end time for desired records
        :return: List of PerformanceData objects representing rows in
          performance_data table
        """
        with self._data.session() as session:
             campaigns = session.query(models.PerformanceData). \
                filter(models.PerformanceData.ymdh.between(start, end)).\
                all()

             return campaigns

    def insert_weights(self, weights):
        """
        Insert data into creative_weights table
        :param weights: List of CreativeWeights objects representing rows in
          creative_weights table
        :return:
        """
        with self._data.session() as session:
            session.add_all(weights)
