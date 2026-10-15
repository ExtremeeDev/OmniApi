from flask import Blueprint, jsonify, send_from_directory, request
import os
from data import ALL_ALIENS

api_bp = Blueprint('api', __name__)

# 1. Home Route
@api_bp.route('/', methods=['GET'])
def home():
    return jsonify({
        "name": "OmniApi",
        "developer": "@ExtremeeDev",
        "status": "Online",
        "endpoints": {
            "all_aliens": "/api/aliens",
            "specific_alien": "/api/aliens/<alien_name>"
        }
    })

# 2. Get All Aliens
@api_bp.route('/api/aliens', methods=['GET'])
def get_aliens():
    return jsonify({
        "total": len(ALL_ALIENS),
        "aliens": ALL_ALIENS
    })

# 3. Get Specific Alien by Name
@api_bp.route('/api/aliens/<string:alien_name>', methods=['GET'])
def get_alien_by_name(alien_name):
    # Name ko lowercase mein match kar rahe hain (heatblast == Heatblast)
    alien = next((a for a in ALL_ALIENS if a['name'].lower() == alien_name.lower()), None)
    if alien:
        return jsonify(alien)
    return jsonify({"error": "Alien not found!"}), 404

# 4. Serve Images Directly (Jiska humne plan kiya tha)
@api_bp.route('/assets/images/<path:filename>')
def serve_image(filename):
    # OmniApi/assets/images ka correct path nikalna
    current_dir = os.path.dirname(__file__)
    image_dir = os.path.abspath(os.path.join(current_dir, '..', 'assets', 'images'))
    
    return send_from_directory(image_dir, filename)
