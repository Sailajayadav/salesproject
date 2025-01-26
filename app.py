from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            file = request.files['file']
            df = pd.read_csv(file)  # Read the CSV file
            # Process the DataFrame (e.g., display, perform calculations, etc.)
            # For example, you can display the first 5 rows:
            table_html = df.head().to_html()  
            return render_template('index.html', table=table_html)
        except Exception as e:
            return f"Error: {e}"  # Display any errors
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)