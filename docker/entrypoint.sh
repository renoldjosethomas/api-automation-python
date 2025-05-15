#!/bin/bash

# Echo message
echo "Running Robot Framework tests..."

# Run Robot Framework tests
python -m robot -v env:dev -v user1:renauto1 -v user2:renauto2 -i smoke ./api-automation-python/test_cases/

# Optionally, add more commands to be executed after the test
echo "Test run completed"