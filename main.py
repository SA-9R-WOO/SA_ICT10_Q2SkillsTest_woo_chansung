from pyscript import display, document

# note to self skibidi toilet 67676767 i love ict
aircraft_info = {
    "c172": {
        "name": "Cessna 172",
        "description": "A reliable trainer plane, the most popular plane in this school.",
        "cruise_speed": "122 knots",
        "range": "640 NM",
        "seating": "4"
    },
    "c152": {
        "name": "Cessna 152",
        "description": "Lightweight two-seater, perfect if you want to get your license without overspending.",
        "cruise_speed": "107 knots",
        "range": "415 NM",
        "seating": "2"
    },
    "piper": {
        "name": "Piper PA-28",
        "description": "Another popular light plane used for private flying and flight school.",
        "cruise_speed": "112 knots",
        "range": "500 NM",
        "seating": "4"
    },
    "": {
        "name": "",
        "description": "",
        "cruise_speed": "",
        "range": "",
        "seating": ""
    }
}

def show_aircraft_info(e):
    document.getElementById('aircraft-info').innerHTML = " "
    selected_aircraft = document.getElementById("aircraft-select").value
    info = aircraft_info.get(selected_aircraft, aircraft_info[""])
            
    output = f"""
            {info['name']}
            Description: {info['description']}
            Cruise Speed: {info['cruise_speed']}
            Range: {info['range']}
            Seating Capacity: {info['seating']}
            """
    display(output, target="aircraft-info")
