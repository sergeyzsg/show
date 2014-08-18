#!/bin/bash

rm -rf $(dirname $0)/env

virtualenv $(dirname $0)/env -p python3
