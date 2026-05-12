def validate_event(event):
    """
    Valida estructura mínima de un evento.

    Inputs:
        event: dict

    Returns:
        bool
    """

    required_fields = [
        "Evento",
        "Zona",
        "Precio",
        "Horario",
        "Descripcion",
        "Ambiente"
    ]

    for field in required_fields:

        if field not in event:
            return False

        if not event[field]:
            return False

    return True
