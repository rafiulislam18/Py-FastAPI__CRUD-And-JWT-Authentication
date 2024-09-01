# Lesson Name : Declare a path parameter
# Note : Then create a path parameter with a type annotation using the enum class you created (ModelName).

from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

"""
The value of the path parameter will be an enumeration member.
You can compare it with the enumeration member in your created enum ModelName

You can get the actual value (a str in this case) using model_name.value, or in general, your_enum_member.value .

You can return enum members from your path operation, even nested in a JSON body (e.g. a dict).
They will be converted to their corresponding values (strings in this case) before returning them to the client.

In your client you will get a JSON response like:
{
  "model_name": "alexnet",
  "message": "Deep Learning FTW!"
}
"""
