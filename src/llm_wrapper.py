import os
import litellm
from typing import List, Dict, Any

# Disable logging for litellm to keep it quiet
litellm.set_verbose = False

def get_api_key(provider: str) -> str:
    """
    Retrieves the API key for a given provider.
    Checks provider-specific keys first, then falls back to LLM_API_KEY.
    """
    provider_keys = {
        "anthropic": "ANTHROPIC_API_KEY",
        "openai": "OPENAI_API_KEY",
        "google": "GOOGLE_API_KEY",
    }
    
    # 1. Check provider-specific key
    env_var = provider_keys.get(provider.lower())
    if env_var:
        key = os.environ.get(env_var)
        if key:
            return key.strip()
            
    # 2. Fallback to generic LLM_API_KEY
    generic_key = os.environ.get("LLM_API_KEY")
    if generic_key:
        return generic_key.strip()
        
    return ""

def call_llm_with_tools(
    provider: str,
    model: str,
    messages: List[Dict[str, str]],
    tools: List[Dict[str, Any]],
    tool_choice: Dict[str, Any],
    max_tokens: int = 4000
) -> Dict[str, Any]:
    """
    Standardized wrapper for calling LLMs with tools using litellm.
    """
    api_key = get_api_key(provider)
    
    # Construct the model string for litellm if needed
    # litellm expects "anthropic/claude-3-haiku-20240307" or "openai/gpt-4o"
    # if the provider prefix is already there, use it.
    model_full = model
    if "/" not in model:
        model_full = f"{provider}/{model}"

    try:
        response = litellm.completion(
            model=model_full,
            messages=messages,
            tools=tools,
            tool_choice=tool_choice,
            max_tokens=max_tokens,
            api_key=api_key
        )
        
        # litellm returns a response object similar to OpenAI's
        # Extract the tool call input
        message = response.choices[0].message
        if hasattr(message, "tool_calls") and message.tool_calls:
            # Return the arguments of the tool call
            import json
            return json.loads(message.tool_calls[0].function.arguments)
        
        raise RuntimeError(f"LLM ({model_full}) did not return a tool call.")
        
    except Exception as e:
        raise RuntimeError(f"Error calling LLM via litellm: {str(e)}")
