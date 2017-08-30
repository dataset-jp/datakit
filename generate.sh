mkdir data

docker-compose run importer bash -l -c "python jp/python/bank/all.py"
mv data/output.csv data/bank_all.csv

docker-compose run importer bash -l -c "python jp/python/currency/jpy_usd_daily.py"
mv data/output.csv data/currency_jpy_usd_daily.csv

docker-compose run importer bash -l -c "python jp/python/land/points_yearly.py"
mv data/output.csv data/land_points_yearly.csv

docker-compose run importer bash -l -c "python jp/python/population/yearly.py"
mv data/output.csv data/population_yearly.csv

docker-compose run importer bash -l -c "python jp/python/postalcode/all.py"
mv data/output.csv data/postalcode_all.csv

docker-compose run importer bash -l -c "python jp/python/stock/ni255_daily.py"
mv data/output.csv data/stock_ni255_daily.csv