import logging
import json
from typing import Any, Dict, List, Tuple, Set, DefaultDict
from collections import defaultdict

from shazam_charts.results import ChartResults, StateChartResults


def parse_line(line: str, line_number: int) -> Dict[str, str or int]:
    """
    Method to extract the useful data
    :param line: The line as a string object
    :param line_number: The line number that is being parsed
    :return: A dictionary of the parsed data
    """

    # define the object to use
    record: Dict[str, str or int] = {}

    # try to load the line
    try:
        data: Any = json.loads(line)
    except json.decoder.JSONDecodeError:
        # if the line isn't valid JSON, return an empty record
        logging.debug(f"JSON Decode Error! Failed to  line {line_number}. Skipping")
        return record

    song_info: Any = data.get("match", {}).get("track", {})
    location_info: Any = data.get("geolocation", {}).get("region", {})
    record["tag_id"] = data.get("tagid")

    if not song_info:
        # the data is essentially useless without this
        # also to skip unnecessary processing
        return record
    else:
        record["song_id"] = song_info.get("id")
        record["song_title"] = song_info.get("metadata", {}).get("tracktitle", "")
        record["song_artist"] = song_info.get("metadata", {}).get("artistname", "")

    if location_info:
        record["country"] = location_info.get("country", "")
        record["state"] = location_info.get("locality")

    return record


def update_song_metadata(
    index: Dict[int, Dict[str, str]], new_song: Dict[str, str or int]
) -> Dict[int, Dict[str, str]]:

    if new_song.get("song_id") in index:
        return index

    index[new_song["song_id"]] = {
        "title": new_song["song_title"],
        "artist": new_song["song_artist"],
    }

    return index


def update_state_chart(
    new_song: Dict[str, str or int], chart: Dict[str, DefaultDict[int, int]]
) -> Dict[str, DefaultDict[int, int]]:
    # if there's no location data, set state to Undefined
    if not new_song.get("country") == "United States":
        state: str = "Undefined"
    else:
        state: str = new_song.get("state", "Undefined")

    # initialise region
    if state not in chart:
        logging.debug(f"Adding state: {state}")
        chart[state] = defaultdict(int)

    # add song info to data
    chart[state][new_song["song_id"]] += 1  # type: ignore

    return chart


def transform(method: str, count: int, filename: str = "shazam_charts/shazam-tag-data.jsonl") -> None:
    """
    Main method to call from the CLI
    1. read file
    2. parse line by line to get useful information
    3. update structure holding information
    4. log it out to the terminal
    :param filename: The filename of the data source
    :param method: The method to be used
    :param count: The total count to be returned
    :return: Nothing
    """

    # if not method == "chart":
    #     raise NotImplementedError(f"Method {method} has not been implemented")

    # data structures for different methods
    song_metadata: Dict[int, Dict[str, str]] = {}
    chart: DefaultDict[int, int] = defaultdict(int)  # {song_id: count}
    state_chart: Dict[str, DefaultDict[int, int]] = {}  # {state: {song_id: count}}

    # read source file and begin extracting
    with open(file=filename, mode="r") as f:
        tag_ids: Set[str] = set()
        for n, line in enumerate(f.readlines()):

            # read line
            processed_line: Dict[str, str] = parse_line(line=line, line_number=n)

            # check that lines are being processed
            if n % 1000 == 0 and n != 0:
                logging.debug(f"Read {n} lines")

            # skip to next line if there is no data
            if not processed_line:
                continue

            # there is a chance for duplicate tag ids so will be skipped
            # sets have constant look up but O(n) space complexity so may consider
            # making this check optional with a CLI option
            if processed_line["tag_id"] in tag_ids:
                continue

            # update song metadata if needed
            song_metadata = update_song_metadata(index=song_metadata, new_song=processed_line)

            # add song info to data
            if method == "chart":
                chart[processed_line["song_id"]] += 1  # type: ignore
            elif method == "state_chart":
                state_chart = update_state_chart(chart=state_chart, new_song=processed_line)

    if method == "chart":
        # sort the chart
        sorted_charts: List[Tuple[int, int]] = sorted(chart.items(), key=lambda x: x[1], reverse=True)  # type: ignore

        # print the chart data
        logging.info(ChartResults(records=sorted_charts, count=count, song_metadata=song_metadata))

    elif method == "state_chart":
        # sorting is handled in the function
        logging.info(StateChartResults(records=state_chart, count=count, song_metadata=song_metadata))

    return
