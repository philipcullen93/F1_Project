from models.circuits import Circuits


def process_circuits(api_response):

    circuits = []

    circuit_list = (
        api_response["MRData"]
        ["CircuitTable"]
        ["Circuits"]
    )

    for circuit_data in circuit_list:

        location = circuit_data["Location"]

        circuit = Circuits(
            circuit_id=circuit_data["circuitId"],
            name=circuit_data.get("circuitName"),
            locality=location.get("locality"),
            country=location.get("country"),
            latitude=location.get("lat"),
            longitude=location.get("long"),
            url=circuit_data.get("url")
        )

        circuits.append(circuit)

    return circuits