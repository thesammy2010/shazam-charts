import unittest
from collections import defaultdict
from typing import Any, Dict, DefaultDict

from shazam_charts.transform import update_song_metadata, update_state_chart


class MyTestCase(unittest.TestCase):

    def test_update_song_metadata1(self):

        raw: Dict[int, Dict[str, str]] = {
            1: {
                "title": "foo",
                "artist": "bar"
            }
        }
        inp: Dict[str, int or str] = {
            "song_id": 2,
            "song_title": "Leo",
            "song_artist": "Data"
        }
        expected_result: Dict[int, Dict[str, str]] = {
            1: {
                "title": "foo",
                "artist": "bar"
            },
            2: {
                "title": "Leo",
                "artist": "Data"
            }
        }

        self.assertDictEqual(expected_result, update_song_metadata(index=raw, new_song=inp))

    def test_update_song_metadata2(self) -> None:
        raw: Dict[int, Dict[str, str]] = {
            1: {
                "title": "foo",
                "artist": "bar"
            },
            2: {
                "title": "Leo",
                "artist": "Data"
            }
        }
        inp: Dict[str, int or str] = {
            "song_id": 2,
            "song_title": "Leo",
            "song_artist": "Data"
        }
        expected_result: Dict[int, Dict[str, str]] = {
            1: {
                "title": "foo",
                "artist": "bar"
            },
            2: {
                "title": "Leo",
                "artist": "Data"
            }
        }

        self.assertDictEqual(expected_result, update_song_metadata(index=raw, new_song=inp))

    def test_update_state_chart1(self) -> None:

        d1: DefaultDict[int, int] = defaultdict(int)
        d1[1] = 25
        d2: DefaultDict[int, int] = defaultdict(int)
        d2[1] = 2
        d3: DefaultDict[int, int] = d1
        d3[2] = 1

        raw: Dict[str, DefaultDict[int, int]] = {
            "New York": d1,
            "California": d2
        }
        inp: Dict[str, int or str] = {
            "song_id": 2,
            "song_title": "Leo",
            "song_artist": "Data",
            "country": "United States",
            "state": "New York"
        }
        expected_result: Dict[str, DefaultDict[int, int]] = {
            "New York": d3,
            "California": d2
        }
        self.assertDictEqual(expected_result, update_state_chart(chart=raw, new_song=inp))

    def test_update_state_chart2(self) -> None:

        d1: DefaultDict[int, int] = defaultdict(int)
        d1[1] = 25
        d2: DefaultDict[int, int] = defaultdict(int)
        d2[1] = 2
        d3: DefaultDict[int, int] = d1
        d3[1] = 26

        raw: Dict[str, DefaultDict[int, int]] = {
            "New York": d1,
            "California": d2
        }
        inp: Dict[str, int or str] = {
            "song_id": 1,
            "song_title": "Leo",
            "song_artist": "Data",
            "country": "United States",
            "state": "New York"
        }
        expected_result: Dict[str, DefaultDict[int, int]] = {
            "New York": d3,
            "California": d2
        }
        self.assertDictEqual(expected_result, update_state_chart(chart=raw, new_song=inp))