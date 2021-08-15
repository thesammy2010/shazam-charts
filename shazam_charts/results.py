from typing import Dict, List, Tuple


class ChartResults(object):
    """
    Class to represent the output nicely in the terminal
    """

    def __init__(
        self, records: List[Tuple[int, int]], song_metadata: Dict[int, Dict[str, str]], count: int = 0
    ) -> None:
        self.count: int = count
        self.song_counts: List[Tuple[int, int]] = records
        self.song_metadata: Dict[int, Dict[str, str]] = song_metadata
        self._max_len: int = len(self.song_counts)

    def __repr__(self) -> str:
        lines: List[str] = []
        for n in range(1, self.count + 1):
            if n > self._max_len:
                break
            song_id: int = self.song_counts[n - 1][0]
            song_info = self.song_metadata[song_id]

            lines.append("%-5i%-40s%-40s" % (n, song_info.get("title"), song_info.get("artist")))
        return "\n".join(lines)

    def __str__(self) -> str:
        return self.__repr__()
