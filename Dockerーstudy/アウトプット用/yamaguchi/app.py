from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/bmi")
def bmi():
    height = request.args.get("height")
    weight = request.args.get("weight")

    height = float(height)
    weight = float(weight)

    height_m = height / 100.0
    bmi_value = weight / (height_m ** 2)

    return jsonify({
        "height": height,
        "weight": weight,
        "bmi": round(bmi_value, 2),
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)