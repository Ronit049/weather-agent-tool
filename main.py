from weather_schema import weather_tool_schema
from weather_tool import (
    get_current_weather,
    weather_data_call
)
from executor import execute_tool_call


tool_registry = {
    "get_current_weather": get_current_weather
}


print("SCHEMA (what LLM sees):")
print(f"Name : {weather_tool_schema['name']}")
print(f"Description : {weather_tool_schema['description']}")
print(
    f"Parameters : "
    f"{list(weather_tool_schema['parameters']['properties'].keys())}"
)


print("\nFUNCTION")
result = get_current_weather("Jaipur")
print(result)


print("\nEXECUTOR")

llm_decided_to_call = {
    "tool_name": "get_current_weather",
    "args": {
        "city": "Mumbai"
    }
}

exec_result = execute_tool_call(
    llm_decided_to_call["tool_name"],
    llm_decided_to_call["args"],
    tool_registry
)

print(exec_result)