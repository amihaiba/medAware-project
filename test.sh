#!/bin/bash
curl -X POST 127.0.0.1:5000 -H 'Content-Type: application/json' -d '{"is_db":1,"file_name":"file1.txt"}'
