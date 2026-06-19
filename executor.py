import json


def execute_tool_call(tool_name: str,
                      tool_args: dict,
                      tool_registry: dict) -> str:

    fn = tool_registry.get(tool_name)

    if fn is None:
        return f"Error: Tool '{tool_name}' not found in registry"

    try:
        result = fn(**tool_args)
        return json.dumps(result, indent=2)

    except TypeError as e:
        return f"Error: Bad arguments for '{tool_name}': {e}"

    except Exception as e:
        return f"Error: Tool execution failed: {e}"