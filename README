# qs

Accepts urls from a filename and, for each query parameter, replace the value
with a specified value.

## Usage

Example input file:

```
~ % cat urls.txt
https://www.evildojo.com/index.php?q=search&name=darkmage
https://www.evildojo.com/index.php?q=search
https://www.evildojo.com/index.php
https://www.evildojo.com
```

Example usage:

```
python3 -m qs urls.txt d3v
https://www.evildojo.com/index.php?q=d3v
https://www.evildojo.com/index.php?q=d3v&name=darkmage
https://www.evildojo.com/index.php?q=search&name=d3v
```

