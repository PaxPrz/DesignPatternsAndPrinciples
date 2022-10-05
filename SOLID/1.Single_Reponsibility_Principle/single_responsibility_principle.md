# Single Responsibility Principle

### Before
```mermaid
classDiagram
    class Employee
    Employee: +str name
    Employee: -str dob
    Employee: +get_age()
    Employee: +print_timesheet_report()
```

Instead of keeping everything inside one class.
Employee class must only be responsible for storing/processing 
employee related data, rather than timesheet of employee.


### After
```mermaid
classDiagram
    class Employee
    Employee: +str name
    Employee: -str dob
    Employee: +get_age()

    class TimesheetReport
    TimesheetReport: +print_timesheet_report(employee)

    TimesheetReport --> Employee
```

Here responsibility is seperated to another TimesheetReport class.
So Employee class is only responsible for storing employee data but not
processing employee data

