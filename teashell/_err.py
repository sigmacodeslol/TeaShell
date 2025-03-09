class Terminate(Exception):
    """Custom exception for handling termination scenarios in TeaShell."""
    def __init__(self, message="Shell terminated", code=0):
        self.code = code
        super().__init__(message)