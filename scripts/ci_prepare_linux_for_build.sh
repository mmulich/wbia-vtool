#!/bin/bash

set -ex

# See https://stackoverflow.com/a/246128/176882
export CUR_LOC="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

$CUR_LOC/_install_opencv_dependencies_apt_on_linux.sh
