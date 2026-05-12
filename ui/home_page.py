import streamlit as st

from config import (
    APP_TITLE,
    APP_SUBTITLE,
    VALID_BUDGETS,
    VALID_ZONES,
    VALID_SCHEDULES,
    SUCCESS_MESSAGE,
    EMPTY_FILTER_MESSAGE,
    LOADING_MESSAGE,
    ERROR_SAVING_PLAN
)

from data.mock_events import EVENTS
from data.models import save_plan, fetch_saved_plans

from logic.event_filters import filter_events
from logic.event_validators import validate_event

from external.logger import log_error


def render_filters():
    """
    Renderiza filtros laterales.
    """

    st.sidebar.title("Filtrar planes")

    budget = st.sidebar.selectbox(
        "Presupuesto",
        VALID_BUDGETS,
        help="Filtra planes según cuánto quieres gastar."
    )

    zone = st.sidebar.selectbox(
        "Zona",
        VALID_ZONES,
        help="Reduce tiempo de traslado eligiendo una zona cercana."
    )

    schedule = st.sidebar.selectbox(
        "Horario",
        VALID_SCHEDULES,
        help="Explora planes diurnos o nocturnos."
    )

    return budget, zone, schedule


def render_event_card(event):
    """
    Renderiza tarjeta individual de evento.
    """

    with st.container(border=True):

        st.markdown(f"## {event['Evento']}")
        st.write(event["Descripcion"])

        col1, col2, col3 = st.columns(3)

        col1.metric("Zona", event["Zona"])
        col2.metric("Precio", event["Precio"])
        col3.metric("Horario", event["Horario"])

        st.caption(f"Ambiente: {event['Ambiente']}")

        save_button = st.button(
            f"Guardar plan · {event['Evento']}",
            use_container_width=True
        )

        if save_button:

            with st.spinner("Guardando tu plan..."):

                try:

                    save_plan(
                        event["Evento"],
                        event["Zona"],
                        event["Precio"]
                    )

                    st.success(SUCCESS_MESSAGE)
                    st.toast("Plan agregado a tus guardados.")

                except Exception as error:

                    st.error(ERROR_SAVING_PLAN)
                    st.error(log_error(str(error)))


def render_saved_plans():
    """
    Renderiza sección de planes guardados.
    """

    st.divider()

    st.header("Tus planes guardados")

    placeholder = st.empty()

    try:

        with st.spinner("Cargando tus planes..."):

            saved_plans = fetch_saved_plans()

        if saved_plans.empty:

            placeholder.info(
                "Todavía no has guardado planes."
            )

        else:

            placeholder.dataframe(
                saved_plans,
                use_container_width=True
            )

    except Exception as error:

        placeholder.error(log_error(str(error)))


def render_home_page():
    """
    Renderiza página principal completa.
    """

    st.title(APP_TITLE)
    st.subheader(APP_SUBTITLE)

    st.info(
        "La mayoría de eventos en Santo Domingo aparecen tarde "
        "o con poca información. Aquí puedes explorarlos con más claridad."
    )

    budget, zone, schedule = render_filters()

    loading_placeholder = st.empty()

    with loading_placeholder.container():

        with st.spinner(LOADING_MESSAGE):

            filtered_events = filter_events(
                EVENTS,
                budget,
                zone,
                schedule
            )

    loading_placeholder.empty()

    if not filtered_events:

        st.warning(EMPTY_FILTER_MESSAGE)

    else:

        for event in filtered_events:

            is_valid = validate_event(event)

            if not is_valid:

                st.error(
                    "Uno de los eventos tiene información incompleta."
                )

                continue

            render_event_card(event)

    render_saved_plans()
