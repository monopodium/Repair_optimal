kill -9 $(pidof memcached)

{
./memcached/bin/memcached -m 128 -p 8000 --max-item-size=5242880 -vv -d
./memcached/bin/memcached -m 128 -p 8001 --max-item-size=5242880 -vv -d
./memcached/bin/memcached -m 128 -p 8002 --max-item-size=5242880 -vv -d
./memcached/bin/memcached -m 128 -p 8003 --max-item-size=5242880 -vv -d
./memcached/bin/memcached -m 128 -p 8004 --max-item-size=5242880 -vv -d
./memcached/bin/memcached -m 128 -p 8005 --max-item-size=5242880 -vv -d
./memcached/bin/memcached -m 128 -p 8006 --max-item-size=5242880 -vv -d
./memcached/bin/memcached -m 128 -p 8007 --max-item-size=5242880 -vv -d
./memcached/bin/memcached -m 128 -p 8008 --max-item-size=5242880 -vv -d
./memcached/bin/memcached -m 128 -p 8009 --max-item-size=5242880 -vv -d
} &> /dev/null
