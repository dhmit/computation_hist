#!/bin/bash
# https://stackoverflow.com/questions/6626351/how-to-extract-bits-from-return-code-number-in-bash
# exit with rc if fatal or error message; but exit 0 if warning, etc.
set -o errexit
set -o nounset
(
    rc=0;
    pylint apps utilities || rc=$?;
    exit $(( $rc & 35 )) # fatal=1 | error=2 | usage error=32
)

