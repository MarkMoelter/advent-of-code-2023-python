import logging

logger = logging.getLogger(__name__)


class Part1:
    def __init__(self, input_file: list[str]) -> None:
        self.input_file = input_file
        self._time_record = self.time_record

    @property
    def time_record(self) -> list[tuple]:

        out = []
        for line in self.input_file:
            line = line.split()
            line.pop(0)
            out.append(list(map(int, line)))

        return [i for i in zip(out[0], out[1])]
