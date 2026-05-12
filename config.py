from pathlib import Path

APP_TITLE = "QueHacerSD"

APP_SUBTITLE = (
    "Descubre planes en Santo Domingo con información clara "
    "de precio, ambiente y ubicación."
)

DATABASE_PATH = Path("/tmp/quehacersd.db")

VALID_BUDGETS = [
    "Todos",
    "RD$500",
    "RD$800",
    "RD$1500"
]

VALID_ZONES = [
    "Todas",
    "Zona Colonial",
    "Piantini",
    "Villa Mella"
]

VALID_SCHEDULES = [
    "Todos",
    "Diurno",
    "Nocturno"
]

SUCCESS_MESSAGE = (
    "Tu plan fue guardado. Ahora puedes volver más tarde "
    "sin perder la información."
)

EMPTY_FILTER_MESSAGE = (
    "No encontramos planes con esos filtros. "
    "Prueba otra combinación."
)

LOADING_MESSAGE = "Cargando planes disponibles..."

ERROR_SAVING_PLAN = (
    "No pudimos guardar el plan en este momento."
)
