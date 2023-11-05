This project is an attempt to use immudb Vault.

The project includes a simple application that allows you to keep a teacher's grade books.

Teachers can create new books, insert grades, view grades, improve grades and delete the entire book.

Students and their parents have read-only access, so they can only view grades

Structure of files:
- src/gradeBook.py - application implementation
- src/config.py - some configuration settings
- credentials.py - credential settings, you can use environment variables instead (IMMUDB_VALUT_API_KEY and IMMUDB_VALUT_API_KEY_READONLY)
- api_test.py - application API tests
- e2e_test.py - application  End to End tests
- helepr.py - supporting functions used in tests

To run all tests use cmd: py.test -v -s --html=report.html

