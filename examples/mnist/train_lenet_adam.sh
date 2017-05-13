#!/usr/bin/env sh
set -e

./caffe train --solver=lenet_solver_adam.prototxt $@
