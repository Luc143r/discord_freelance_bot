from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/create_guild&guild={name_guild}&name={name}&discr={discr}")
async def create_guild(name_guild: str, name: str, discr: str):
    dict_guilds = {
        "type_req": "create",
        "name_guild": name_guild,
        "name": name,
        "discr": discr
    }
    json_dump = json.dumps(dict_guilds, indent=4)
    with open("logs.json", "w") as json_file:
        json_file.write(json_dump)
    return {"method": "create_guild", "guild": dict_guilds}


@app.get("/delete_guild&guild={name_guild}")
async def delete_guild(name_guild: str):
    dict_guilds = {
        "type_req": "delete",
        "name_guild": name_guild
    }
    json_dump = json.dumps(dict_guilds, indent=4)
    with open("logs.json", "w") as json_file:
        json_file.write(json_dump)
    return {"method": "delete_guild", "guild": dict_guilds}


@app.get("/add_user&guild={name_guild}&name={name}&discr={discr}")
async def add_user(name_guild: str, name: str, discr: str):
    dict_guilds = {
        "type_req": "add",
        "name_guild": name_guild,
        "name": name,
        "discr": discr
    }
    json_dump = json.dumps(dict_guilds, indent=4)
    with open("logs.json", "w") as json_file:
        json_file.write(json_dump)
    return {"method": "add_user", "guild": dict_guilds}


@app.get("/del_user&guild={name_guild}&name={name}&discr={discr}")
async def del_user(name_guild: str, name: str, discr: str):
    dict_guilds = {
        "type_req": "remove",
        "name_guild": name_guild,
        "name": name,
        "discr": discr
    }
    json_dump = json.dumps(dict_guilds, indent=4)
    with open("logs.json", "w") as json_file:
        json_file.write(json_dump)
    return {"method": "del_user", "guild": dict_guilds}


@app.get("/rename_guild&old_name={old_name}&new_name={new_name}")
async def rename_guild(old_name: str, new_name: str):
    dict_guilds = {
        "type_req": "rename",
        "old_name": old_name,
        "new_name": new_name
    }
    json_dump = json.dumps(dict_guilds, indent=4)
    with open("logs.json", "w") as json_file:
        json_file.write(json_dump)
    return {"method": "rename_guild", "guild": dict_guilds}
