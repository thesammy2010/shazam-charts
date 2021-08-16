from unittest import TestCase

from shazam_charts.results import ChartResults, StateChartResults


class TestResults(TestCase):
    def test_chart_result_1_record(self) -> None:

        chart: ChartResults = ChartResults(
            records=[(340816375, 5)],
            count=1,
            song_metadata={340816375: {"title": "Believer", "artist": "Imagine Dragons"}},
        )
        expected_result: str = "%-5i%-40s%-40s" % (1, "Believer", "Imagine Dragons")
        calculated_result: str = str(chart)
        self.assertEqual(expected_result, calculated_result)

    def test_chart_result_1_records(self) -> None:
        chart: ChartResults = ChartResults(
            records=[(340816375, 5), (1234, 4)],
            count=1,
            song_metadata={
                340816375: {"title": "Believer", "artist": "Imagine Dragons"},
                1234: {"title": "Foo", "artist": "Bar"},
            },
        )
        expected_result: str = "%-5i%-40s%-40s" % (1, "Believer", "Imagine Dragons")
        calculated_result: str = str(chart)
        self.assertEqual(expected_result, calculated_result)

    def test_chart_result_count_greater(self) -> None:

        chart: ChartResults = ChartResults(
            records=[(340816375, 5), (1234, 4)],
            count=3,
            song_metadata={
                340816375: {"title": "Believer", "artist": "Imagine Dragons"},
                1234: {"title": "Foo", "artist": "Bar"},
            },
        )
        expected_result: str = "%-5i%-40s%-40s\n%-5i%-40s%-40s" % (1, "Believer", "Imagine Dragons", 2, "Foo", "Bar")
        calculated_result: str = str(chart)
        self.assertEqual(expected_result, calculated_result)

    def test_state_chart_result_count_1(self) -> None:

        chart: StateChartResults = StateChartResults(
            records={"New York": {340816375: 5}, "Illinois": {1234: 4}},
            count=1,
            song_metadata={
                340816375: {"title": "Believer", "artist": "Imagine Dragons"},
                1234: {"title": "Foo", "artist": "Bar"},
            },
        )

        expected_result: str = "\nIllinois\n%-5i%-50s%-50s\n\nNew York\n%-5i%-50s%-50s" % (
            1,
            "Foo",
            "Bar",
            1,
            "Believer",
            "Imagine Dragons",
        )
        calculated_result: str = str(chart)
        self.assertEqual(expected_result, calculated_result)

    def test_state_chart_results_count_1(self) -> None:

        chart: StateChartResults = StateChartResults(
            records={"New York": {340816375: 5, 0: 1000}, "Illinois": {1234: 4, 0: 1}},
            count=1,
            song_metadata={
                340816375: {"title": "Believer", "artist": "Imagine Dragons"},
                1234: {"title": "Foo", "artist": "Bar"},
                0: {"title": "Leo", "artist": "Data"},
            },
        )

        expected_result: str = "\nIllinois\n%-5i%-50s%-50s\n\nNew York\n%-5i%-50s%-50s" % (
            1,
            "Foo",
            "Bar",
            1,
            "Leo",
            "Data",
        )
        calculated_result: str = str(chart)
        self.assertEqual(expected_result, calculated_result)

    def test_state_chart_results_count_count_greater(self) -> None:

        chart: StateChartResults = StateChartResults(
            records={"New York": {340816375: 5, 0: 1000}, "Illinois": {1234: 4, 0: 1}},
            count=5,
            song_metadata={
                340816375: {"title": "Believer", "artist": "Imagine Dragons"},
                1234: {"title": "Foo", "artist": "Bar"},
                0: {"title": "Leo", "artist": "Data"},
            },
        )

        expected_result: str = (
            "\nIllinois\n%-5i%-50s%-50s\n%-5i%-50s%-50s\n\nNew York\n%-5i%-50s%-50s\n%-5i%-50s%-50s"
        ) % (1, "Foo", "Bar", 2, "Leo", "Data", 1, "Leo", "Data", 2, "Believer", "Imagine Dragons")
        calculated_result: str = str(chart)
        self.assertEqual(expected_result, calculated_result)
