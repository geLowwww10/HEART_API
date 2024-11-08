from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample heart information
heart_info = [
    {
        "heart_id": "10",
        "date": "November 09, 2024",
        "heart_rate": "271 rate"
    },
    {
        "heart_id": "11",
        "date": "November 09, 2024",
        "heart_rate": "300 rate"
    }
]

@app.route('/heart', methods=["GET", "POST"])
def getHeart():
    if request.method == "GET":
        return jsonify(heart_info)
    elif request.method == "POST":
        new_heart = request.get_json()
        heart_info.append(new_heart)
        return jsonify({"message": "Heart Information Added successfully"}), 200


@app.route("/heart/<heart_id>", methods=["GET"])
def get_heart_by_id(heart_id):
    heart = next((item for item in heart_info if item["heart_id"] == heart_id), None)
    if heart:
        return jsonify(heart), 200
    else:
        return jsonify({"error": "Heart Information not found"}), 404

@app.route("/heart/<heart_id>", methods=["PUT"])
def update_heart(heart_id):
    heart = next((item for item in heart_info if item["heart_id"] == heart_id), None)
    if heart:
        updated_data = request.get_json()
        if "date" in updated_data:
            heart["date"] = updated_data["date"]
        if "heart_rate" in updated_data:
            heart["heart_rate"] = updated_data["heart_rate"]
        
        return jsonify({"message": "Heart Information updated successfully"}), 200
    else:
        return jsonify({"error": "Heart Information not found"}), 404


@app.route("/heart/<heart_id>", methods=["DELETE"])
def delete_heart(heart_id):
    heart = next((item for item in heart_info if item["heart_id"] == heart_id), None)
    
    if heart:
        heart_info.remove(heart)
        return jsonify({"message": "Heart Information deleted successfully"}), 200
    else:
        return jsonify({"error": "Heart Information not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
