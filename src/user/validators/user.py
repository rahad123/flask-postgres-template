from pydantic import BaseModel, create_model


class Person(BaseModel):
    name: str
    age: int


# Define the data schema as a dictionary and this is function base
# user_data_schema = {
#     'name': (int, ...),        # Tuple format: (data_type, validation_rules)
#     'age': (int, ...),
# }

# Create a Pydantic model dynamically using create_model
# Person = create_model('Person', **user_data_schema)
