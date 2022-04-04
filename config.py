
class Settings():

    # ELasticsearch
    ES_URL: str = 'http://192.168.4.150:9200'
    INDEX: str = 'car_index'

    # Postgresql
    PG_HOST: str = '192.168.4.150'
    PG_PORT: str = '5432'
    PG_USER: str = 'acome'
    PG_PASSWORD: str = 'isicod5321'
    PG_DATABASE_NAME: str = 'acome'


settings = Settings()
