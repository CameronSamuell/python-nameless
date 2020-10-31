__version__ = '1.753.20'
try:
    from ._nameless import longest  # noqa
except ImportError:
    def longest(args):
        return max(args, key=len)
