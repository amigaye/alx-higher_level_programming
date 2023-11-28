#!/usr/bin/python3
def copy_list(l): return l.copy() if hasattr(l, 'copy') else list(l)
