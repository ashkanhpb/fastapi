from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

costs_list = {}


@app.get("/costs/get_all_costs")
def get_costs():
    return costs_list


@app.get("/costs/get_single_cost")
def get_cost(cost_id: int):
    if cost_id not in costs_list:
        return JSONResponse({"message": "Cost not found"}, status_code=404)
    return costs_list[cost_id]


@app.post("/costs/add_cost")
def add_costs(cost_id: int, description: str, amount: float):
    if cost_id not in costs_list:
        costs_list[cost_id] = {"description": description, "amount": amount}
        return JSONResponse(status_code=201, content=costs_list)
    return JSONResponse({"message": "CostID is duplicate"}, status_code=406)


@app.delete("/costs/delete_cost")
def delete_cost(cost_id: int):
    if cost_id not in costs_list:
        return JSONResponse({"message": "Cost not found"}, status_code=404)
    else:
        costs_list.pop(cost_id)
    return JSONResponse(status_code=204, content=costs_list)


@app.put("/costs/edit_cost")
def edit_cost(cost_id: int, description: str, amount: float):
    if cost_id not in costs_list:
        return JSONResponse({"message": "Cost not found"}, status_code=404)
    costs_list[cost_id] = {"description": description, "amount": amount}
    return JSONResponse(status_code=202, content=costs_list)
