from abc import ABC, abstractmethod
from typing import Protocol, Any


class DataProcessor(ABC):

    _data: dict[int, str]

    def __init__(self) -> None:
        self._data = {}

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self._data) == 0:
            raise Exception(f"Output error: data processor "
                            f"{self.__class__.__name__} is empty")
        key: int = list(self._data.keys())[0]
        value: str | None = self._data.get(key)
        self._data.pop(key)
        if value is None:
            raise Exception("output error value is None")
        return (key, value)


class NumericProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        match type(data).__name__:
            case 'int':
                return True
            case 'float':
                return True
            case 'list':
                for d in data:
                    if type(d) is not int and type(d) is not float:
                        return False
                return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:

        match type(data).__name__:
            case 'int':
                self._data.update({len(self._data): str(data)})
            case 'float':
                self._data.update({len(self._data): str(data)})
            case 'list':
                # mypy [union-attr]: see documentation
                # -> mypy.readthedocs.io/en/stable/error_code_list.html
                assert isinstance(data, list)
                values: list[int | float] = data
                for value in values:
                    if self.validate(value) is False:
                        raise Exception("Improper numeric data")
                    k: int = len(self._data)
                    v: str = str(value)
                    self._data.update({k: v})
            case _:
                raise Exception("Improper numeric data")


class TextProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        match type(data).__name__:
            case 'str':
                return True
            case 'list':
                for value in data:
                    if type(value) is not str:
                        return False
                return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        match type(data).__name__:
            case 'str':
                self._data.update({len(self._data): str(data)})
            case 'list':
                for value in data:
                    if self.validate(value) is False:
                        raise Exception("Improper text data")
                    key: int = len(self._data)
                    self._data.update({key: value})
            case _:
                raise Exception("Improper text data")


class LogProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        match type(data).__name__:
            case 'dict':
                if 'log_level' not in data or 'log_message' not in data:
                    return False
                if len(data) != 2:
                    return False
                for x in data:
                    if type(x) is not str or type(data.get(x)) is not str:
                        return False
                return True
            case 'list':
                for value in data:
                    if type(value) is not dict:
                        return False
                    if 'log_level' not in value or 'log_message' not in value:
                        return False
                    if len(value) != 2:
                        return False
                    for x in value:
                        if type(x) is not str or type(value.get(x)) is not str:
                            return False
                return True
            case _:
                return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        match  type(data).__name__:
            case 'dict':
                if self.validate(data) is False:
                    raise Exception("Improper log data")
                assert isinstance(data, dict)
                value: dict[str, str] = data

                log_level: str | None = value.get('log_level')
                log_message: str | None = value.get('log_message')
                self._data.update(
                    {len(self._data): f"{log_level}: {log_message}"})
            case 'list':
                if self.validate(data) is False:
                    raise Exception("Improper log data")
                assert isinstance(data, list)
                for value in data:
                    log_level = value.get('log_level')
                    log_message = value.get('log_message')
                    self._data.update(
                        {len(self._data): f"{log_level}: {log_message}"})
            case _:
                raise Exception("Improper log data")


class DataStream:

    __proc: list[DataProcessor]
    __numeric_data: dict[str, int]
    __text_data: dict[str, int]
    __log_data: dict[str, int]

    def __init__(self) -> None:
        self.__proc = []
        self.__numeric_data = {'processed': 0, 'remaining': 0}
        self.__text_data = {'processed': 0, 'remaining': 0}
        self.__log_data = {'processed': 0, 'remaining': 0}

    def get_proc(self) -> list[DataProcessor]:
        return self.__proc

    def register_processor(self, proc: DataProcessor) -> None:
        self.__proc.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            proc: DataProcessor | None = None
            for processor in self.__proc:
                if processor.validate(item) is True:
                    proc = processor
            if proc is None:
                print("DataStream error - "
                      f"Can't process element in stream: {item}")
            else:
                proc.ingest(item)
                if isinstance(proc, NumericProcessor) is True:
                    processed: int = self.__numeric_data['processed']
                    + len(item) if isinstance(item, list) is True else\
                        self.__numeric_data['processed'] + 1
                    remaining: int = self.__numeric_data['remaining']
                    + len(item) if isinstance(item, list) is True else\
                        self.__numeric_data['remaining'] + 1
                    self.__numeric_data.update({'processed': processed})
                    self.__numeric_data.update({'remaining': remaining})
                if isinstance(proc, TextProcessor) is True:
                    value = self.__text_data['processed']
                    + len(item) if isinstance(item, list) is True else\
                        self.__text_data['processed'] + 1
                    remaining = self.__text_data['remaining']
                    + len(item) if isinstance(item, list) is True else\
                        self.__text_data['remaining'] + 1
                    self.__text_data.update({'processed': value})
                    self.__text_data.update({'remaining': remaining})
                if isinstance(proc, LogProcessor) is True:
                    value = self.__log_data['processed']
                    + len(item) if isinstance(item, list) is True else\
                        self.__log_data['processed'] + 1
                    remaining = self.__log_data['remaining']
                    + len(item) if isinstance(item, list) is True else\
                        self.__log_data['remaining'] + 1
                    self.__log_data.update({'processed': value})
                    self.__log_data.update({'remaining': remaining})

    def print_processors_stats(self) -> None:
        print("== DataStream statistic")
        if len(self.__proc) == 0:
            print("No processor found, no data")
        for proc in self.__proc:
            if isinstance(proc, NumericProcessor):
                proc_type: str = 'Numeric'
                total: int = self.__numeric_data['processed']
                remaining: int = self.__numeric_data['remaining']
            if isinstance(proc, TextProcessor):
                proc_type = 'Text'
                total = self.__text_data['processed']
                remaining = self.__text_data['remaining']
            if isinstance(proc, LogProcessor):
                proc_type = 'Log'
                total = self.__log_data['processed']
                remaining = self.__log_data['remaining']
            print(f"{proc_type} Processor: total {total} items processed, "
                  f"remaining {remaining} on processor")

    def consume_data(self, stream: DataProcessor) -> tuple[int, str]:
        data: tuple[int, str] = stream.output()
        if isinstance(stream, NumericProcessor):
            remaining: int = self.__numeric_data['remaining'] - 1
            self.__numeric_data.update({'remaining': remaining})
        if isinstance(stream, TextProcessor):
            remaining = self.__text_data['remaining'] - 1
            self.__text_data.update({'remaining': remaining})
        if isinstance(stream, LogProcessor):
            remaining = self.__log_data['remaining'] - 1
            self.__log_data.update({'remaining': remaining})
        return data


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")

    print("Initialize Data Stream...")
    stream: DataStream = DataStream()
    stream.print_processors_stats()
    print("\nRegistering Numeric Processor")
    numeric_processor: NumericProcessor = NumericProcessor()
    stream.register_processor(numeric_processor)
    data_batch: list[Any] = ['Hello world',
                                    [3.14, -1, 2.71],
                                    [{'log_level': 'WARNING',
                                     'log_message':
                                        'Telnet access! Use ssh instead'},
                                     {'log_level': 'INFO',
                                     'log_message': 'User wil isconnected'}],
                                    42, ['Hi', 'five']]
    print(f"Send first batch of data "
          f"on stream: {data_batch}")
    stream.process_stream(data_batch)
    stream.print_processors_stats()

    print("Registering other data processors")
    text_processor: TextProcessor = TextProcessor()
    log_processor: LogProcessor = LogProcessor()
    stream.register_processor(text_processor)
    stream.register_processor(log_processor)
    print("Send the same batch again")
    stream.process_stream(data_batch)
    stream.print_processors_stats()
    print("Consume some elements from "
          "the data processors: Numeric 3, Text 2, Log 1")
    try:
        stream.consume_data(numeric_processor)
        stream.consume_data(numeric_processor)
        stream.consume_data(numeric_processor)
        stream.consume_data(text_processor)
        stream.consume_data(text_processor)
        stream.consume_data(log_processor)
    except Exception as e:
        print(e)
    stream.print_processors_stats()
