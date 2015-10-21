from datetime import datetime
import random
from flask import Blueprint

mod_two = Blueprint('ali', __name__)

def int_checker(func):
    def wrapper(*args, **kwargs):
        try:
            int(kwargs['num_max'])
            return func(kwargs['num_max'])
        except Exception:
            return 'Invalid Input!'
        finally:
            pass        
    return wrapper


@mod_two.route('/simple_random_with_check/<num_max>')
@int_checker
def simple_random_with_check(num_max):
    num = int(num_max)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return 'Randomized ' + str(random.randint(1, num)) + ' at ' + current_time
