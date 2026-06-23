#!/bin/sh

time=$(date +'%Y%m%d-%H:%M:%S')

python3 -m pytest tests/test_api_ui_integration.py -v >./logs/unittest_${time}.logs
python3 -m pytest tests/test_data_driven.py -v >>./logs/unittest_${time}.logs
python3 -m pytest tests/test_httpbin.py -v >>./logs/unittest_${time}.logs
python3 -m pytest tests/test_saucedemo_api.py -v >>./logs/unittest_${time}.logs
