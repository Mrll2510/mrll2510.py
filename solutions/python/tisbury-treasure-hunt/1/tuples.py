"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    Parameters:
        record (tuple): A (treasure, coordinate) pair.

    Returns:
        str: The extracted map coordinate.
    """
    
    return record[1]
    
print(get_coordinate(("Scrimshawed Whale Tooth", "2A")))

def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    Parameters:
        coordinate (str): A string map coordinate.

    Returns:
        tuple: The string coordinate split into its individual components.
    """

    return (coordinate[0], coordinate[1]) 

print(convert_coordinate("2A"))


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, tuple(coordinate_1, coordinate_2), quadrant) trio.

    Returns:
        bool: Do the coordinates match?
    """

    coordenada_azarra = azara_record[1]
    coordenada_rui = rui_record[1]

    coordenada_azarra_convet = convert_coordinate(coordenada_azarra)

    return coordenada_azarra_convet == coordenada_rui

print(compare_records(("Brass Spyglass", "4B"), ("Seaside Cottages", ("1", "C"), "blue")))
print(compare_records(("Model Ship in Large Bottle", "8A"), ("Harbor Managers Office", ("8", "A"), "purple")))

def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    Parameters:
        azara_record (tuple): A (treasure, coordinate) pair.
        rui_record (tuple): A (location, coordinate, quadrant) trio.

    Returns:
        tuple or str: The combined record (if compatible), or the string "not a match" (if incompatible).
    """
    coordenada_azarra = azara_record[1]
    coordenada_rui = rui_record[1]

    coordenada_azarra_convert = convert_coordinate(coordenada_azarra)

    if coordenada_azarra_convert == coordenada_rui:
        novatupla = (azara_record[0], azara_record[1], rui_record[0], rui_record[1], rui_record[2])
        return novatupla
    return "not a match"

print(create_record(("Brass Spyglass", "4B"), ("Abandoned Lighthouse", ("4", "B"), "Blue")))
print(create_record(("Brass Spyglass", "4B"), ("Seaside Cottages", ("1", "C"), "blue")))
        
def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    Parameters:
        combined_record_group (tuple): Everything from both participants.

    Returns:
        str: Everything "cleaned", excess coordinates and information are removed.

    Note:
        The return statement is a multi-lined string with items separated by newlines.
        (see HINTS.md for an example).

    """
    relatorios = []
    
    for registro in combined_record_group:
        linha = f"('{registro[0]}', '{registro[2]}', {registro[3]}, '{registro[4]}')"
        relatorios.append(linha)
    
    return "\n".join(relatorios) + "\n"

print(clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'))))