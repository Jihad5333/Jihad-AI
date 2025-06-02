from dashboard import create_app
import os

for folder in ["tasks", "logs", "actions"]:
    os.makedirs(folder, exist_ok=True)

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
