class EntryAttr:
    def __init__(self) -> None: ...

class ProbabilityEntry(EntryAttr):
    def __init__(self, probability) -> None: ...

class CountFilterEntry(EntryAttr):
    def __init__(self, count_filter) -> None: ...

class ShowClickEntry(EntryAttr):
    def __init__(self, show_name, click_name) -> None: ...
