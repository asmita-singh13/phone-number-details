from flask import Flask, request, render_template
import phonenumbers
from phonenumbers import geocoder, carrier

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    details = {}
    if request.method == "POST":
        phone_number = request.form.get("phone_number")
        try:
            parsed_number = phonenumbers.parse(phone_number)
            details = {
                "Location": geocoder.description_for_number(parsed_number, "en"),
                "Carrier": carrier.name_for_number(parsed_number, "en"),
                "Valid": phonenumbers.is_valid_number(parsed_number),
                "Number Type": phonenumbers.number_type(parsed_number),
            }
        except Exception as e:
            details = {"Error": str(e)}
    return render_template("index.html", details=details)

if __name__ == "__main__":
    app.run(debug=True)