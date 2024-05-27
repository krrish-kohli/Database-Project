class InvalidStateException(Exception):
    """
    Exception raised when the state of a system is 
    not appropriate for a method call.
    """
    def __init__(self, message="Invalid state for operation"):
        self.message = message
        super().__init__(self.message)