## python_guard: An automatic test setup for python

### Setup

- Copy the `Gemfile` and `Guardfile` into your python project directory.
- Bundle install (this requires ruby, the best method is to install via rvm)
- Run guard `bundle exec guard` (some text editors offer a Guard plugin)

Whilst this is running, guard watches your project so that each time you save a project file it will run the corresponding tests, and send a notification (via guard on mac or libnotify on linux) how many tests passed and failed.

For example, if you save b/c.py, guard will run tests following (if they exist) tests/b/test_c.py, tests/test_c.py b/tests/c.py b/test_c.py.