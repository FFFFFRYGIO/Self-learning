from os import getenv

postgresql = {
    'pguser': getenv('pguser'),
    'pgpasswd': getenv('pgpasswd'),
    'pghost': getenv('pghost'),
    'pgport': getenv('pgport'),
    'pgdb': getenv('pgdb'),
    }
