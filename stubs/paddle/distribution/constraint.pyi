from _typeshed import Incomplete

class Constraint:
    def __call__(self, value) -> None: ...

class Real(Constraint):
    def __call__(self, value): ...

class Range(Constraint):
    def __init__(self, lower, upper) -> None: ...
    def __call__(self, value): ...

class Positive(Constraint):
    def __call__(self, value): ...

class Simplex(Constraint):
    def __call__(self, value): ...

real: Incomplete
positive: Incomplete
simplex: Incomplete
