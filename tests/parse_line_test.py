import unittest
from typing import Any, Dict

from shazam_charts.transform import parse_line


class TestParseLine(unittest.TestCase):
    def test_1(self) -> None:
        raw: str = "{}"
        expected_result: Dict[str, Any] = {"tag_id": None}
        calculated_result: Dict[str, Any] = parse_line(line=raw, line_number=0)
        self.assertDictEqual(expected_result, calculated_result)

    def test_2(self) -> None:
        raw: str = "{test}"
        expected_result: Dict[str, Any] = {}
        calculated_result: Dict[str, Any] = parse_line(line=raw, line_number=0)
        self.assertDictEqual(expected_result, calculated_result)

    def test_3(self) -> None:
        raw: str = '{"tagid": "12AB"}'
        expected_result: Dict[str, Any] = {"tag_id": "12AB"}
        calculated_result: Dict[str, Any] = parse_line(line=raw, line_number=0)
        self.assertDictEqual(expected_result, calculated_result)

    def test_4(self) -> None:
        raw: str = """
        {
            "match":{
                "track":{
                    "id":340816375,
                    "metadata":{
                        "artistname":"Imagine Dragons",
                        "tracktitle":"Believer"
                    },
                    "offset":195.252
                }
            }
        }
        """
        expected_result: Dict[str, Any] = {
            "tag_id": None,
            "song_id": 340816375,
            "song_title": "Believer",
            "song_artist": "Imagine Dragons",
        }
        calculated_result: Dict[str, Any] = parse_line(line=raw, line_number=0)
        self.assertDictEqual(expected_result, calculated_result)

    def test_5(self) -> None:
        raw: str = """
        {
            "geolocation":{

            },
            "match":{
                "track":{
                    "id":340816375,
                    "metadata":{
                        "artistname":"Imagine Dragons",
                        "tracktitle":"Believer"
                    },
                    "offset":195.252
                }
            }
        }
        """
        expected_result: Dict[str, Any] = {
            "tag_id": None,
            "song_id": 340816375,
            "song_title": "Believer",
            "song_artist": "Imagine Dragons",
        }
        calculated_result: Dict[str, Any] = parse_line(line=raw, line_number=0)
        self.assertDictEqual(expected_result, calculated_result)

    def test_6(self) -> None:

        raw: str = """
        {
            "geolocation":{
                "zone":"IL",
                "region":{
                    "locality":"Illinois",
                    "country":"United States"
                }
            },
            "match":{
                "track":{
                    "id":340816375,
                    "metadata":{
                        "artistname":"Imagine Dragons",
                        "tracktitle":"Believer"
                    },
                    "offset":195.252
                }
            }
        }
        """
        expected_result: Dict[str, Any] = {
            "tag_id": None,
            "song_id": 340816375,
            "song_title": "Believer",
            "song_artist": "Imagine Dragons",
            "country": "United States",
            "state": "Illinois",
        }
        calculated_result: Dict[str, Any] = parse_line(line=raw, line_number=0)
        self.assertDictEqual(expected_result, calculated_result)
