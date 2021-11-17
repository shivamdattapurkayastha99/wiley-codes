# SQL Query
#1. Find the second largest salary in the table
# SELECT max(empsal) from emp where empsal<(SELECT MAX(empsal) where empsal<max(empsal) from emp)
# 2.Insert values into a table
# INSERT INTO table values (val1,val2)
# INSERT INTO table (job) values (val1)

