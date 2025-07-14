from flask import Flask, request, jsonify, abort
import random
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

def generate_city_data(city):
    return {
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
            "Known for its homos and lesbos",
            "Renowned for its art galleries.",
            "Has a vibrant nightlife.",
            "Home to a famous university."
        ])
    }

@app.route('/city/<string:city>/population', methods=['GET'])
def get_population(city):
    """Get the population of a city
    ---
    parameters:
      - name: city
        in: path
        type: string
        required: true
        description: Name of the city
    responses:
      200:
        description: Population data
        schema:
          type: object
          properties:
            city:
              type: string
            population:
              type: integer
      400:
        description: Bad Request
    """
    if not city:
        abort(400, description="City name is required in the path.")
    data = generate_city_data(city)
    return jsonify({"city": city, "population": data["population"]}), 200

@app.route('/city/<string:city>/area', methods=['GET'])
def get_area(city):
    """Get the area of a city in km²
    ---
    parameters:
      - name: city
        in: path
        type: string
        required: true
        description: Name of the city
    responses:
      200:
        description: Area data
        schema:
          type: object
          properties:
            city:
              type: string
            area_km2:
              type: number
              format: float
      400:
        description: Bad Request
    """
    if not city:
        abort(400, description="City name is required in the path.")
    data = generate_city_data(city)
    return jsonify({"city": city, "area_km2": data["area_km2"]}), 200

@app.route('/city/<string:city>/fun-fact', methods=['GET'])
def get_fun_fact(city):
    """Get a fun fact about a city
    ---
    parameters:
      - name: city
        in: path
        type: string
        required: true
        description: Name of the city
    responses:
      200:
        description: Fun fact
        schema:
          type: object
          properties:
            city:
              type: string
            fun_fact:
              type: string
      400:
        description: Bad Request
    """
    if not city:
        abort(400, description="City name is required in the path.")
    data = generate_city_data(city)
    return jsonify({"city": city, "fun_fact": data["fun_fact"]}), 200

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
