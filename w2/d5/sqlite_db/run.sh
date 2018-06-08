#!/usr/bin/env bash

rm securities_master.db
echo 'Database deleted'
python3 schema.py
echo 'Schema defined'
python3 seed.py
echo 'data seeded'
