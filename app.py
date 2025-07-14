from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/city', methods=['GET'])
def city_info():
    city = request.args.get('name')
    if not city:
        return jsonify({"error": "City name is required as a 'name' query parameter."}), 400

    data = {
        "city": city,
        "population": random.randint(50000, 10000000),
        "area_km2": round(random.uniform(50.0, 10000.0), 2),
        "fun_fact": random.choice([
            "It has more bicycles than cars!",
            "Famous for its local cuisine.",
            "Was founded over 500 years ago.",
            "Hosts an annual music festival.",
            "Has underground shopping streets.",
            "Known for its beautiful parks.",
            "Features a historic castle.",
            "Known for its homos and lesbos"
            "Renowned for its art galleries.",
            "Has a vibrant nightlife.",
            "Home to a famous university."
        ])
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
