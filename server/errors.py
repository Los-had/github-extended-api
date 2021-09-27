def http_error(error):
    return {
        "Message": f"A http_error(error: {error}) ocurred, try again."
    }

def connection_error(error):
    return {
        "Message": f"A connection_error(error: {error}) ocurred, try again."
    }

def default_error():
    return {
        "Message": "An error ocurred, try again."
    }

def dynamic_error(error):
    return {
        "Message": "An error ocurred, try again.",
        "Error": error
    }
