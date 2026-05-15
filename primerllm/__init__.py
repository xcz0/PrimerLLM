import importlib.metadata

try:
    __version__ = importlib.metadata.version("primerllm")
except importlib.metadata.PackageNotFoundError:
    pass
