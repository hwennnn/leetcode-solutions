---
title: SQL Basics
tags:
  - backend
  - database
  - sql
date: 2025-01-29
---

## Create Table

```sql
CREATE TABLE customers (
    first_name VARCHAR(64),
    last_name VARCHAR(64),
    email VARCHAR(64) UNIQUE,
    dob DATE,
    since DATE,
    customerid VARCHAR(16) PRIMARY KEY, -- applies to the row
    country VARCHAR(16)
);

CREATE TABLE games (
    name VARCHAR(32),
    version CHAR(3),
    price NUMERIC NOT NULL,
    PRIMARY KEY (name, version)
);

CREATE TABLE downloads (
    customerid VARCHAR(16) REFERENCES customers (customerid),
    name VARCHAR(32),
    version CHAR(3),
    FOREIGN KEY (name, version) REFERENCES games (name, version)
);
```

## Identify Primary Key

### Column Constraint

```sql
CREATE TABLE customers (
    first_name VARCHAR(64),
    last_name VARCHAR(64),
    email VARCHAR(64),
    dob DATE,
    since DATE,
    customerid VARCHAR(16) PRIMARY KEY, -- applies to the row
    country VARCHAR(16)
);
```

### Table Constraint

```sql
CREATE TABLE customers (
    first_name VARCHAR(64),
    last_name VARCHAR(64),
    email VARCHAR(64),
    dob DATE,
    since DATE,
    customerid VARCHAR(16),
    country VARCHAR(16),
    PRIMARY KEY (customerid) -- after row
);
```

## NOT NULL

```sql
CREATE TABLE games (
    name VARCHAR(32),
    version CHAR(3),
    price NUMERIC NOT NULL,
    PRIMARY KEY (name, version)
);
```

> ⚠️ **Note**: A `NOT NULL` constraint guarantees that no value of the corresponding field in any record of the table can be set to `NULL`. A `NOT NULL` constraint is always declared as a **column constraint**.

### Implicit NULL

```sql
INSERT INTO games (name, version) VALUES ('Game 1', '1.0');
```

### Explicit NULL

```sql
INSERT INTO games VALUES ('Game 1', '1.0', NULL);
```

> [!error]
> Both statements will be rejected. With a `NOT NULL` constraint, you can't insert a row without providing a value for the field.

> [!note]
> If there is a `default` value, you can insert a row without providing a value for the `NOT NULL` field. But still, you can't insert a row with explicit `NULL`.

## Foreign Key

1. `NULL` Customers (but Not in Games)

   ```sql
   INSERT INTO downloads VALUES (NULL, 'Aerified', '1.0');
   -- Allow (NULL) for (customerid)
   ```

2. `NULL` Games (but Not in Customers)

   ```sql
   INSERT INTO downloads VALUES ('1234567890', NULL, '1.0');
   -- Allow (NULL, '1.0') for (name, version)
   ```

> [!note]
> We **omit** the check if any value in the set to be checked is `NULL`. We check all constraints independently and must satisfy all constraints.

## `CHECK` Constraint

```sql
CREATE TABLE games (
    name VARCHAR(32),
    version CHAR(3),
    price NUMERIC NOT NULL,
      CHECK (price > 0),
    PRIMARY KEY (name, version)
);
```

> [!note]
> A `CHECK` constraint is declared as a column or a table constraint with the `CHECK` keyword followed by the SQL condition in parenthesis. If the condition involves more than one column, it should be a table constraint.

### Violate `CHECK` Constraint

```sql
UPDATE games SET price = price - 5.5;
```

> [!error]
> Discounting all the prices by $5.5 creates negative
> prices. This operation will be aborted and rolled
> back.

## Cascade `UPDATE` and `DELETE`

```sql
CREATE TABLE downloads (
    customerid VARCHAR(16)
        REFERENCES customers (customerid)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    name VARCHAR(32),
    version CHAR(3),
    FOREIGN KEY (name, version)
        REFERENCES games (name, version)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
```

> [!note] `ON UPDATE CASCADE` and `ON DELETE CASCADE` propagate the update or deletion.

## `CASE` keyword

We can do this but not preferrable.

```sql
    SELECT name || ' ' || version,
    CASE
        WHEN price * 0.09 >= 0.3 THEN ROUND(price * 1.09, 2)
        ELSE price
    END AS price
    FROM games;
```

## `COALESCE` keyword

`COALESCE(x1, x2, x3, ...)` returns the first `non-NULL` (from left-to-right) of its argument.

- `COALESCE(NULL, 1, NULL, 2)` is `1`.
- `COALESCE(NULL, NULL, NULL)` is `NULL`.

## Counting with `NULL`

- `COUNT(*)` counts `NULL` values.
- `COUNT(att)`, `AVG(att)`, `MAX(att)`, `MIN(attt)` eliminate `NULL` values.

## `JOIN` keyword

### CROSS JOIN vs INNER JOIN

While **inner join** is a popular construct, there is no added expressiveness or performance in **INNER JOIN**.
The two queries below are equivalent.

```sql
-- Inner Join
SELECT *
FROM customers c
    INNER JOIN downloads d
        ON d.customerid = c.customerid
    INNER JOIN games g
        ON d.name = g.name AND d.version = g.version;
```

```sql
-- Cross Join
SELECT *
FROM customers c, downloads d, games g
WHERE d.customerid = c.customerid
    AND d.name = g.name
    AND d.version = g.version;
```

### Natural Join

If we managed to give the same name to columns with the same meaning across the tables, we can use
**natural join**. **NATURAL JOIN** joins rows that have the **same values** for columns with the **same name**. It
also **prints only one** of the two columns.

### Outer Join

WIP

## Good Practices

### Avoid `NULL`

It is generally a good idea to constrain all attributes to be not NULL unless there is a good design or tuning reason for not doing so.

### Justify Cascade

Think carefully about which foreign keys should be subject to cascade.

### Defer Constraints

It is generally a good idea to defer all the constraints that can be deferred. A deferred constraint is checked at the end of a transaction and not immediately after each operation.

### Play the Devil's Advocate

Given the complete schema for the three tables, try and find out the scenario in which an operation (insertion, deletion, update) on a table or a transaction containing a set of operation on one or more tables violate which constraint on which table.
