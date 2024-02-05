#!/usr/bin/env python3
"""
Test module for utils.access_nested_map function.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock
import requests


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test the access_nested_map function.

        Parameters:
        - nested_map: Mapping
            A nested map.
        - path: Sequence
            A sequence of keys representing a path to the value.
        - expected_result: Any
            The expected result returned by the function.

        Returns:
        - None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that access_nested_map raises a KeyError with
        the expected message.

        Parameters:
        - nested_map: Mapping
            A nested map.
        - path: Sequence
            A sequence of keys representing a path to the value.
        Returns:
        - None
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test class for utils.get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that utils.get_json returns the expected result.

        Parameters:
        - test_url: str
            The URL to be passed to get_json.
        - test_payload: dict
            The expected payload returned by the mocked get method.
        """
        mocked_response = Mock()
        mocked_response.json.return_value = test_payload
        with patch('requests.get', return_value=mocked_response) as mocked_get:
            output = get_json(test_url)
        mocked_get.assert_called_once_with(test_url)
        self.assertEqual(output, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test class for utils.memoize decorator.
    """

    class TestClass:
        """
        Test class with a memoized property.
        """

        def a_method(self) -> int:
            """mocked method for testing"""
            return 42

        @memoize
        def a_property(self) -> int:
            """property to be tested using memoize decorator"""
            return self.a_method()

    def test_memoize(self):
        """
        Test that calling a_property twice returns the correct result,
        and a_method is only called once using assert_called_once.
        """
        test_instance = self.TestClass()

        # Mock the a_method
        with patch.object(
                test_instance,
                'a_method',
                return_value=42) as mocked_a_method:
            # Call a_property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Assert that a_method is only called once
            mocked_a_method.assert_called_once()

            # Assert that the results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
