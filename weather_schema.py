weather_tool_schema = {
    "name": "get_current_weather",

    "description": (
        "Get the current weather for a given city. "
        "Use this when the user asks about current weather, temperature, "
        "or weather conditions in any location."
    ),

    "parameters": {
        "type": "object",

        "properties": {
            "city": {
                "type": "string",
                "description": "City name, e.g. 'Jaipur', 'Mumbai', 'Delhi'"
            },

            "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"],
                "description": "Temperature unit. Default: celsius"
            }
        },

        "required": ["city"]
    }
}