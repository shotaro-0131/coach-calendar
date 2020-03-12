#!/bin/sh
# wait-for-postgres.sh

set -e

host="$1"
shift
user="root"

password=""

cmd="$@"

echo "Waiting for mysql"
echo "$user"
echo "$password"
echo "$host" 

sleep 20s
# until mysql -h"$host" -u"$user" -p"$password" &> /dev/null
# do
#         >&2 echo -n "."
#         sleep 1
# done

# >&2 echo "MySQL is up - executing command"
echo "$host" 
exec $cmd
exec "$cmd"