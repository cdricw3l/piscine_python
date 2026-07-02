from abc import ABC, abstractmethod
import typing

class DataProcessor(ABC):
    
    _data: dict[int, str]

    def __init__(self) -> None:
        self._data = {}

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        key: int = list(self._data.keys())[0]
        value: str = self._data.get(key)
        self._data.pop(key)
        return tuple((key, value)) 

class NumericProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()        

    def validate(self, data: typing.Any) -> bool:
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
                for value in data:
                    if self.validate(value) == False :
                        raise Exception("Improper numeric data")
                    key: int = len(self._data)
                    value: str = str(value)
                    self._data.update({key: value})
            case _:
                raise Exception("Improper numeric data")


class TextProcessor(DataProcessor):
    
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
        match type(data).__name__:
            case 'str':
                return True
            case 'list':
                for value in data:
                    if type(value) is not str:
                        return False
                return True
        return False

    def  ingest(self, data: str | list[str]) -> None:
        match type(data).__name__:
            case 'str':
                self._data.update({len(self._data): data})
            case 'list':
                for value in data:
                    if self.validate(value) == False:
                        raise Exception("Improper text data")
                    key: int = len(self._data)
                    self._data.update({key: value})
            case _:
                raise Exception("Improper text data")

class LogProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: typing.Any) -> bool:
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

    def ingest(self, data:  dict[str, str] | list[dict[str, str]]) -> None:
        match  type(data).__name__:
            case 'dict':
                if self.validate(data) == False:
                    raise Exception("Improper log data")
                log_level: str = data.get('log_level')
                log_message: str = data.get('log_message')
                self._data.update({len(self.data): f"{log_level}: {log_message}"})
            case 'list':
                if self.validate(data) == False:
                    raise Exception("Improper log data")
                for value in data:
                    log_level: str = value.get('log_level')
                    log_message: str = value.get('log_message')
                    self._data.update({len(self._data): f"{log_level}: {log_message}"})
            case _:
                raise Exception("Improper log data")

if __name__ == "__main__":
    
    num: NumericProcessor = NumericProcessor()
    text_processor: TextProcessor = TextProcessor()
    log_processor: LogProcessor = LogProcessor()
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    print(f"Trying to validate input '42': {num.validate(42)}")
    print(f"Trying to validate input 'hello': {num.validate('hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num.ingest('foo')
    except Exception as e:
        print(f"Got exception: {e}")
    arr_num: list[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {arr_num}")
    num.validate(arr_num)
    num.ingest(arr_num)
    print("Extracting 3 values...")
    for i in range(3):
        data: tuple[int, str] = num.output()
        print(f"Numeric value {data[0]}: {data[1]}")
    print("\nTesting Text Processor...")
    print(f"Trying to validate input '42': {text_processor.validate(42)}")
    arr_text: list[str]= ["Hello", "Nexus", "World"]
    print(f"Processing data: {arr_text}")
    text_processor.validate(arr_text)
    text_processor.ingest(arr_text)
    print("Extracting 1 values...")
    for i in range(1):
        data: tuple[int, str] = text_processor.output()
        print(f"Text value {data[0]}: {data[1]}")
    print("\nTesting Log Processor...")
    print(f"Trying to validate input 'Hello': {log_processor.validate('Hello')}")
    # assert(log_processor.validate([{"0":"hello", "2": "dqdq"}, {"0":"dqwdwq", "1": "dwqdwq"}]) == False)
    # assert(log_processor.validate("hello berlin") == False)
    # assert(log_processor.validate([{0:"hello", "2": "dqdq"}, {"0":"dqwdwq", "1": "dwqdwq"}]) == False)
    # assert(log_processor.validate({'log_level': "importante", 'log_message':'salut la compagnie'}) == True)
    arr_log: list[dict[str, str]] =  [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                                      {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    #assert(log_processor.validate(arr_log) == True)
    log_processor.ingest(arr_log)
    print("Extracting 2 values...")
    for i in range(2):
        data: tuple[int, str] = log_processor.output()
        print(f"Log entry {data[0]}: {data[1]}")
