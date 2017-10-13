Edit SQL in emacs.

```
pip install emacsql
pip install emacsql catsql[mysql]
pip install emacsql catsql[postgres]
```


```
emacsql test.sqlite3
emacsql test.sqlite3 --table users
emacsql postgres[ql]://user:pass@host/db
emacsql test.sqlite3 --table users --grep paul
```
