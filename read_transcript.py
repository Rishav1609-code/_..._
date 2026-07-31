import json

transcript_path = r"C:\Users\rajvi\.gemini\antigravity-ide\brain\87f6ce16-240a-4311-816a-03bbd0ca1f63\.system_generated\logs\transcript.jsonl"

try:
    with open(transcript_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for line in lines[-150:]:
        try:
            data = json.loads(line)
            if data.get("type") == "USER_INPUT":
                print(f"\n--- USER ---\n{data.get('content')[:300]}")
            elif data.get("type") == "PLANNER_RESPONSE" and data.get("tool_calls"):
                for tc in data["tool_calls"]:
                    print(f"TOOL: {tc['name']} {tc.get('args', {}).get('TargetFile', '')} {tc.get('args', {}).get('CommandLine', '')}")
            elif data.get("type") == "PLANNER_RESPONSE" and data.get("content"):
                print(f"MODEL: {data.get('content')[:150]}")
        except:
            pass
except Exception as e:
    print(f"Error reading transcript: {e}")
