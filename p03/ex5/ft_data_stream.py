import random
import typing


def gen_event(
        list_name: list[str],
        list_action: list[str]) -> typing.Generator[tuple[str, ...]]:
    while list_name and list_action:
        r_name: str = random.choice(list_name)
        r_action: str = random.choice(list_action)
        yield tuple([r_name, r_action])


def consume_event(events: list[tuple[str, ...]]
                  ) -> typing.Generator[tuple[str, ...]]:
    print(f"list event len {len(events)}")
    while events:
        idx: int = random.randrange(len(events))
        value: tuple[str, ...] = events[idx]
        del events[idx]
        yield value


if __name__ == "__main__":
    list_name: list[str] = ["bob", "alice", "dylan"]
    action_list: list[str] = [
        "run", "eat", "sleep", "grab",
        "move", "climb", "sleep", "swim", "release"]
    nb_event: int = 1000
    print("=== Game Data Stream Processor ===")
    gen = gen_event(list_name, action_list)
    for i in range(nb_event):
        try:
            value: tuple[str, ...] = next(gen)
            print(f"Event {i}: Player {value[0]} did action run {value[1]}")
        except (StopIteration, IndexError):
            print("fin de l'iteration")
            break
    gen = gen_event(list_name, action_list)
    list_event: list[tuple[str, ...]] = [next(gen),
                                         next(gen),
                                         next(gen),
                                         next(gen),
                                         next(gen),
                                         next(gen),
                                         next(gen),
                                         next(gen),
                                         next(gen),
                                         next(gen)]
    print(f"\nBuilt list of 10 events: {list_event}\n")
    for event in consume_event(list_event):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {list_event}")
