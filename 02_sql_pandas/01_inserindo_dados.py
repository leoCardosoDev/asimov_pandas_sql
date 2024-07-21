import sqlite3
import pandas as pd
from pathlib import Path

db = Path(__file__).parent / 'web.db'
connection = sqlite3.connect(db)