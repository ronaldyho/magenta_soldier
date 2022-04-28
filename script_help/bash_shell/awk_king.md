
## Select all lines between two marker patterns
https://stackoverflow.com/questions/17988756/how-to-select-lines-between-two-marker-patterns-which-may-occur-multiple-times-w
```
==> /var/log/myPattern <==
2020/01/01 01:01 Log line
2020/01/01 01:01 Log line
2020/01/01 01:01 Log line

==> /var/log/NOT my pattern <==
2020/02/01 02:01 Log line
2020/02/01 02:01 Log line
2020/02/01 02:01 Log line

==> /var/log/myPattern <==
2020/01/01 01:01 Log line
2020/01/01 01:01 Log line
2020/01/01 01:01 Log line
```
`# awk '/var.log.myPattern/{flag=1;next}/==>/{flag=0}flag' myLogs`
```
2020/01/01 01:01 Log line
2020/01/01 01:01 Log line
2020/01/01 01:01 Log line

2020/01/01 01:01 Log line
2020/01/01 01:01 Log line
2020/01/01 01:01 Log line
```

