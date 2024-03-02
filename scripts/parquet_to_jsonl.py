import pyarrow.parquet as pq


# Specify the path to your Parquet file
parquet_file_path = "data/biology.parquet"

# Read the Parquet file
table = pq.read_table(parquet_file_path)

# Convert the table to a Pandas DataFrame
df = table.to_pandas()


# Convert the DataFrame to a JSON string
json_data = df.to_json(orient="records")
json_string = json_data.replace("[", "").replace("]", "")
final_list = json_string.split("},")
# You can also save the JSON data to a file if needed
with open(
    "data/biology.jsonl", "w"
) as json_file:
    for json_dict in final_list:
        if not json_dict.endswith("}"):
            json_file.write(json_dict.replace("topic;", "topic") + "}\n")
        else:
            json_file.write(
                json_dict.replace("topic;", "topic").replace("'", '"') + "\n"
            )
