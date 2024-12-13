/usr/bin/env bash

# Thông số kết nối
HOST="localhost"   # hoặc địa chỉ IP máy chủ
PORT="5432"         # cổng mặc định của PostgreSQL là 5432
USER="tiger"
DATABASE="tiger"

# Thực thi lệnh psql
psql -h "$HOST" -p "$PORT" -U "$USER" -d "$DATABASE"