# datakit
  Currently datakit is a assemble of methods to preprocess open data. A preprocessing open data is a something all we do. Even if we share same aim, source codes are not shared so much. It’s nice idea to refrain it as open source project.

We appreciate these values: 
- Latest data
- Cleaned data (unixtime, UTF-8, without duplicate..)
- Support major formats(csv, json, xml, hdf)
- Community based

# Try it on your local
    $ mkdir data
    $ docker-compose run importer bash -l -c "python jp/python/bank/all.py"
    $ cat data/output.csv

# feature works
- provide framework for preprocessing data.
- allow user to select which and how data column will be composed.



