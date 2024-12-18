from flask import Blueprint, render_template, jsonify
import random
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

nba_api_bp = Blueprint('nba_api', __name__)

@nba_api_bp.route('/nba/<player_id>')
def player_stats(player_id):
    # Use the NBA API to get player stats
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_data = career.get_data_frames()[0]
    
    # Pass the data to the template
    return render_template('nba_page.html', career_data=career_data)

@nba_api_bp.route('/random_player')
def random_player():
    all_players = players.get_active_players()
    random_player = random.choice(all_players)

    player_id = random_player['id']
    player_name = random_player['full_name']

    return jsonify({'name': player_name,
                    'id': player_id
                    })