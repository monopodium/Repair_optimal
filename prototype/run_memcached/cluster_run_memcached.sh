#! /bin/bash
kill -9 $(pidof memcached)

./memcached/bin/memcached -m 1024 -p 31400 --max-item-size=16777216 -d
./memcached/bin/memcached -m 1024 -p 31401 --max-item-size=16777216 -d
./memcached/bin/memcached -m 1024 -p 31402 --max-item-size=16777216 -d
./memcached/bin/memcached -m 1024 -p 31403 --max-item-size=16777216 -d
./memcached/bin/memcached -m 1024 -p 31404 --max-item-size=16777216 -d
./memcached/bin/memcached -m 1024 -p 31405 --max-item-size=16777216 -d
./memcached/bin/memcached -m 1024 -p 31406 --max-item-size=16777216 -d
./memcached/bin/memcached -m 1024 -p 31407 --max-item-size=16777216 -d
./memcached/bin/memcached -m 1024 -p 31408 --max-item-size=16777216 -d
./memcached/bin/memcached -m 1024 -p 31409 --max-item-size=16777216 -d
./memcached/bin/memcached -m 1024 -p 31410 --max-item-size=16777216 -d
./memcached/bin/memcached -m 1024 -p 31411 --max-item-size=16777216 -d
./memcached/bin/memcached -m 1024 -p 31412 --max-item-size=16777216 -d
./memcached/bin/memcached -m 1024 -p 31413 --max-item-size=16777216 -d
./memcached/bin/memcached -m 1024 -p 31414 --max-item-size=16777216 -d
./memcached/bin/memcached -m 1024 -p 31415 --max-item-size=16777216 -d
./memcached/bin/memcached -m 1024 -p 31416 --max-item-size=16777216 -d
./memcached/bin/memcached -m 1024 -p 31417 --max-item-size=16777216 -d
./memcached/bin/memcached -m 1024 -p 31418 --max-item-size=16777216 -d
./memcached/bin/memcached -m 1024 -p 31419 --max-item-size=16777216 -d

