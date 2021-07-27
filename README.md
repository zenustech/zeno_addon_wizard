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