import json


def create_standalone_dashboard():
    """
    Reads model data and an HTML template, injects the data into the template,
    and saves the result as a single, self-contained HTML file.
    """
    json_data_path = 'model_data.json'
    template_path = 'dashboard_template.html'
    output_path = 'dashboard.html'

    print(f"--- Reading data from '{json_data_path}' ---")
    try:
        with open(json_data_path, 'r') as f:
            model_data = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: '{json_data_path}' not found. Please run 'generate_data.py' first.")
        return

    print(f"--- Reading template from '{template_path}' ---")
    try:
        with open(template_path, 'r') as f:
            template_content = f.read()
    except FileNotFoundError:
        print(f"ERROR: '{template_path}' not found. Make sure it's in the same directory.")
        return

    # Convert the Python dictionary to a JSON string for embedding in JavaScript
    json_payload = json.dumps(model_data)

    print("--- Injecting data and creating the final dashboard ---")
    # Replace the placeholder in the template with our actual JSON data
    final_html = template_content.replace('{{JSON_PAYLOAD}}', json_payload)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_html)

    print("\nSUCCESS!")
    print(f"Dashboard created: '{output_path}'")
    print("You can now send this single file to your boss. They just need to double-click it.")


if __name__ == '__main__':
    create_standalone_dashboard()
