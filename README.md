# ZENO Addon Wizard

Demo project showing on how to add custom nodes to ZENO.

# Setup

First of all, run this command:
```bash
git submodule update --init --recursive
```
To fetch ZENO which is included a submodule.

## Build

```bash
cmake -B build
cmake --build build --parallel
```

## Run

```bash
./run.py
```

# Coding

The `YourProject/` is a demo project for showing how to add custom nodes in ZENO.

See [MyPrimitiveOps.cpp](YourProject/MyPrimitiveOps.cpp) for custom primitive operation.
See [CustomNumber.cpp](YourProject/CustomNumber.cpp) for defining custom object.
