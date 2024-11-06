import warnings

def suppress_warnings():
    warnings.filterwarnings('ignore')
    warnings.warn = lambda *args, **kwargs: None