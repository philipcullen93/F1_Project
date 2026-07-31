from models.constructor import Constructor

def process_constructors(api_response):

    constructors = []

    constructor_list = (
        api_response["MRData"]
        ["ConstructorTable"]
        ["Constructors"]
    )

    for constructor_data in constructor_list:

        constructor = Constructor(
            constructor_id = constructor_data["constructorId"],
            name = constructor_data["name"],
            nationality = constructor_data.get("nationality"),
            url = constructor_data.get("url")
        )

        constructors.append(constructor)

    return constructors