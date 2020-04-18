# Hello gRPC

A simple implement of gRPC in Python.


## Quickstart

### Step 1: Create virtualenv

```shell
$ cd hello
$ virtualenv -p python3 hello-venv
$ source hello-venv/bin/activate
$ pip install -r requirements.txt
```

### Step 2: Generate gRPC python code 

```shell
$ cd hello
$ PROTOS_DIR_IN=./protos
$ PROTOS_DIR_OUT=.
$ python3 -m grpc_tools.protoc -I $PROTOS_DIR_IN --python_out=$PROTOS_DIR_OUT --grpc_python_out=$PROTOS_DIR_OUT $PROTOS_DIR_IN/hello.proto
```

### Step 3: Test gRPC application

Start gRPC server

```shell
python3 hello_server.py
```

Start a client in python

```shell
python3 hello_client.py

# Result
# Hello client received: Hello gRPC, Quan Vu!
```

### Finish



