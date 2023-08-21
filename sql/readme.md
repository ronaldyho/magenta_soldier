# Retrieve all entries in a table 
```
`SELECT TABLE_NAME, TABLE_ROWS FROM `information_schema`.`tables` WHERE `table_schema` = 'YOUR_DB_NAME';
```

## Accurate count of all rows in a table 

```sql
SET @tableSchema = 'TARGET_DATABASE';
SET SESSION group_concat_max_len = 10000000;
SET @rowCounts = (
  SELECT group_concat(CONCAT('SELECT ''',TABLE_NAME,''', COUNT(*) FROM ', TABLE_NAME) SEPARATOR ' union all ')
  FROM information_schema.tables 
  WHERE table_schema = @tableSchema AND TABLE_TYPE = 'BASE TABLE'
);
PREPARE statement FROM @rowCounts;
EXECUTE statement;

-- don't run dealloc until you've exported your results ;)
DEALLOCATE PREPARE statement;
```
