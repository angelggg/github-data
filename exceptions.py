

class CrawlerValidationException(Exception):
    """Will be raised when params don't match the expectations"""
    pass

class Not200Exception(Exception):
    """Will be raised when not getting 200 code where it should"""
    pass
