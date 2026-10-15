# @ExtremeeDev On Telegram 

import os
import importlib

def load_all_aliens():
    aliens_list = []
    current_dir = os.path.dirname(__file__)
    aliens_dir = os.path.join(current_dir, 'aliens')
    
    # Aliens folder ke andar ki saari .py files check karega
    for filename in os.listdir(aliens_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f"data.aliens.{filename[:-3]}"
            module = importlib.import_module(module_name)
            
            # Agar file mein alien_data hai, toh list mein daal dega
            if hasattr(module, 'alien_data'):
                aliens_list.append(module.alien_data)
    
    # ID ke hisaab se sort kar dega (1, 2, 3...)
    return sorted(aliens_list, key=lambda x: x['id'])

ALL_ALIENS = load_all_aliens()
