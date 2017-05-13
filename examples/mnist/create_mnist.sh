#!/usr/bin/env sh
# This script converts the mnist data into lmdb/leveldb format,
# depending on the value assigned to $BACKEND.
set -e

EXAMPLE=examples/mnist
DATA=data/mnist


BACKEND="lmdb"

echo "Creating ${BACKEND}..."

rm -rf mnist_train_${BACKEND}
rm -rf mnist_test_${BACKEND}

./convert_mnist_data.bin train-images-idx3-ubyte \
  train-labels-idx1-ubyte mnist_train_${BACKEND} --backend=${BACKEND}
./convert_mnist_data.bin t10k-images-idx3-ubyte \
  t10k-labels-idx1-ubyte mnist_test_${BACKEND} --backend=${BACKEND}

echo "Done."
