def format_pnr_response(data):

    if not data:
        return "PNR number not found."

    seat = data["seat"] if data["seat"] else "not assigned"

    return f"""
    Your ticket is {data['status']}.
    Train {data['train']}.
    Seat {seat}.
    """


def format_train_response(data):

    if not data:
        return "Train number not found."

    return f"""
    Train {data['name']} runs from
    {data['from']} to {data['to']}.
    """