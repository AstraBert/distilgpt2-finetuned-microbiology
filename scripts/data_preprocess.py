import json


def parse_jsonl(jsonl_file_path, **kwargs):
    file = open(jsonl_file_path, "r")
    lines = file.readlines()
    file.close()
    field = "None"
    filter = "None"
    list_of_dicts = []
    for key, value in kwargs.items():
        if key == "field":
            field = value
        elif key == "filt":
            filter = value
        else:
            raise ValueError("Allowed kwargs are field and filter")
    if field == "None" and filter == "None":
        for line in lines:
            json_object = json.loads(line)
            list_of_dicts.append(json_object)
        return list_of_dicts
    elif (field == "None" and filter != "None") or (
        field != "None" and filter == "None"
    ):
        raise ValueError("You cannot set filter without field or field without filter")
    else:
        for line in lines:
            json_object = json.loads(line)
            if json_object[field] == filter:
                list_of_dicts.append(json_object)
            else:
                continue
        return list_of_dicts


def write_jsonl_file(json_obj_list, output_jsonl):
    jsonl = open(output_jsonl, "w")
    for json_obj in json_obj_list:
        line = json.dumps(json_obj)
        jsonl.write(line + "\n")


# Specify the path to your JSONL file
jsonl_file_path = "data/biology.jsonl"
outjson = "data/microbiology.jsonl"
l = parse_jsonl(jsonl_file_path, field="topic", filt="Microbiology")
write_jsonl_file(l, outjson)
