from dataclasses import dataclass
from typing import Any


@dataclass
class Employee:
    name: str
    __age: str

    def get_age(self) -> int:
        ...

    def print_timesheet_report(self) -> str:
        ...


"""
Instead of keeping everything inside one class.
Employee class must only be responsible for storing/processing 
employee related data, rather than timesheet of employee.
"""


@dataclass
class Employee:
    name: str
    __age: str

    def get_age(self) -> str:
        ...


class TimesheetReport:
    def print_timesheet_report(self, employee: Employee) -> Any:
        ...


"""
Here responsibility is seperated to another TimesheetReport class.
So Employee class is only responsible for storing employee data but not
processing employee data
"""
