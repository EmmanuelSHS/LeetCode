#!/bin/bash
echo 'test this is  a test' | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{print $2, $1}'
