"""Functions used in preparing Guido's gorgeous lasagna."""

# Constantes
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calcula o tempo restante de forno."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calcula o tempo de preparo em minutos."""
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calcula o tempo total gasto em minutos."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time