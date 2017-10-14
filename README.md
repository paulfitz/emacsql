emacsql
===

Edit slices of SQL tables in emacs.  Just specify a table and any filters
you want to apply, and the table will show up in emacs in csv format.
Any edits you make will be applied back to the original source.

## Install

To edit local Sqlite databases, just do:

```
pip install emacsql
```

For PostgreSQL or MySQL support, add `catsql[postgres]` or `catsql[mysql]`:

```
pip install emacsql catsql[mysql]
pip install emacsql catsql[postgres]
```

For other databases, just install the appropriate [SQLAlchemy dialect](http://docs.sqlalchemy.org/en/latest/dialects/index.html).

## Use

```
emacsql test.sqlite3
emacsql test.sqlite3 --table users
emacsql postgres[ql]://user:pass@host/db --table users
emacsql mysql://user:pass@host/db --table users
emacsql test.sqlite3 --table users --grep paul
emacsql test.sqlite3 --table comments --sql "length(txt) < 40"
```

For all filters, see https://github.com/paulfitz/catsql#examples

