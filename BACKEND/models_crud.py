from extensions import db
from sqlalchemy import text, exc
 
def create_user_tables():
    user_table_sql = text("""
        CREATE TABLE IF NOT EXISTS Task (
        `taskId` INT AUTO_INCREMENT PRIMARY KEY,
        `name` VARCHAR(255),
        `description` TEXT,
        `points` INT,
        `image_url` TEXT
        )ENGINE=InnoDB;
    """)

    with db.engine.begin() as connection:
        connection.execute(user_table_sql)
 
def initialize_database():
    """Create user tables if they don't exist before the first request."""
    create_user_tables()
