from datetime import datetime
import random
from flask import Blueprint

mod = Blueprint('ruth', __name__)

@mod.route('/simple_random/<num_max>')
def simple_random(num_max):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return 'Randomized ' + str(random.randint(1, num_max)) + ' at ' + current_time
    