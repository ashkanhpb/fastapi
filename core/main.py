from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import List

from models.cost import Cost

app = FastAPI()

costs_list: list[Cost] = []


@app.get("/costs/get_all_costs" ,  response_model=List[Cost])
def get_costs():
    return costs_list


@app.get("/costs/get_single_cost")
def get_cost(cost_id: int):
    for cost in costs_list:
        if cost.cost_id == cost_id:
            return cost

    raise HTTPException(
        status_code=404,
        detail="Cost not found"
    )


@app.post("/costs/add_cost" ,  response_model=List[Cost])
def add_costs(cost: Cost):
    for c in costs_list:
        if c.cost_id == cost.cost_id:
            return JSONResponse({"message": "CostID is duplicate"}, status_code=406)
    costs_list.append(cost)
    return costs_list





@app.delete("/costs/delete_cost")
def delete_cost(cost_id: int):
    for cost in costs_list:
        if cost.cost_id == cost_id:
            costs_list.remove(cost)
            return JSONResponse(status_code=201, content=costs_list)
        else:
            return JSONResponse({"message": "Cost not found"}, status_code=404)


@app.put("/costs/edit_cost")
def edit_cost(cost: Cost):
    for c in costs_list:
        if c.cost_id==Cost.cost_id:
                costs_list.remove(c)
                costs_list.append(cost)
                return JSONResponse(status_code=202, content=costs_list)
    return JSONResponse({"message": "Cost not found"}, status_code=404)


