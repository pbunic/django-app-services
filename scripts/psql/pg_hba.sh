#!/bin/sh

# host-based authentication
sed -i 's/host all all all scram-sha-256/host all all 172.24.0.1\/16 scram-sha-256/g' \
/var/lib/postgresql/data/pg_hba.conf