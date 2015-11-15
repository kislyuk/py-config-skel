# py-config-skel
Python helper class to ingest and serialize app-specific configuration

Provides a self-contained (no dependencies outside the standard library), Python 2 and 3 compatible configuration
    manager. Automatically saves and restores your application's configuration in your user home directory. Uses JSON
    for serialization. Supports dict-like methods and access semantics.
    
Examples:
```python
config = Config()
config.host, config.port = "example.com", 9000
config.nested_config = {}
config.nested_config.foo = True
```
After restarting your application:
```python
config = Config()
print(config)
>>> {'host': 'example.com', 'port': 9000, 'nested_config': {'foo': True}}
```
Using an `argparse.Namespace` object returned by `argparse.parse_args()`:
```
parser = argparse.ArgumentParser()
...
args = parser.parse_args()
if args.foo is not None:
    config.foo = args.foo
elif "foo" not in config:
    raise Exception("foo unconfigured")

config.update(vars(args))
```
