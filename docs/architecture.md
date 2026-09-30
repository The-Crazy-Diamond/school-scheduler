# Architecture

This document tracks the architectural decisions of the project.

The architecture will evolve progressively as the requirements become clearer.
The following structure is therefore a possible long-term architecture rather
than the current project structure.

## Possible target architecture

school_scheduler/
│
├── domain/
│   ├── teacher.py
│   ├── room.py
│   ├── course.py
│   ├── school_year.py
│   ├── scenario.py
│   └── schedule.py
│
├── application/
│   ├── school_year_service.py
│   ├── scenario_service.py
│   └── scheduling_service.py
│
├── validation/
│   ├── teacher_rules.py
│   ├── room_rules.py
│   ├── course_rules.py
│   └── validator.py
│
├── optimization/
│   ├── problem.py
│   ├── problem_builder.py
│   │
│   ├── constraints/
│   │   ├── teacher_conflict.py
│   │   ├── room_conflict.py
│   │   ├── availability.py
│   │   └── distribution.py
│   │
│   └── solvers/
│       ├── base.py
│       └── cp_sat.py
│
├── persistence/
│   ├── models.py
│   ├── repositories.py
│   └── database.py
│
├── api/
│   ├── teachers.py
│   ├── school_years.py
│   ├── scenarios.py
│   └── schedules.py
│
├── import_export/
│   ├── csv.py
│   └── excel.py
│
└── tests/
