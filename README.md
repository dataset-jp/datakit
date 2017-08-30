# dataset

    $ docker build -t dataset:importer .
    $ mkdir -p data/jp
    $ docker run -i -t dataset:importer bash -l -c "python /src/jp/bank/all.py"


# Debug
    $ docker ps
    $ docker exec -it cdebd3c2ec80 bash