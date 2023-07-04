'''This file will be used to test Mock() features.'''

import unittest
from unittest.mock import Mock, patch
from requests.exceptions import ConnectionError, Timeout

import data_structures.my_calendar as my_calendar
from data_structures.my_calendar import get_holidays


HOLIDAYS = {'25/12': 'Christmas', '01/01': 'New Years'}


class TestGetHolidays(unittest.TestCase):
    '''This class will test the get_holidays() function.'''

    def log_requests(self, url):
        '''This is a mock function to log requests using static data.'''
        response_mock = Mock(
            **{'json.return_value': HOLIDAYS},
            **{'status_code': 200},
        )
        return response_mock

    @patch.object(my_calendar.requests, 'get', side_effect=ConnectionError)
    def test_get_holidays_connection(self, mocked_get):
        '''Simple test to showcase how to mock a connection error
        mocking the requests.get() function using patch.object().'''
        with self.assertRaises(ConnectionError):
            get_holidays()

    @patch('data_structures.my_calendar.requests', autospec=True)
    def test_requests_get(self, mocked_requests):
        '''Main test case showcasing different mock features.'''
        mocked_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()

        mocked_requests.get.side_effect = self.log_requests # Mock() object
        assert get_holidays()['25/12'] == 'Christmas'
        assert mocked_requests.get.call_count == 2


if __name__ == '__main__':
    unittest.main()