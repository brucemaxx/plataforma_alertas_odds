from pydantic import BaseModel


class JogoSchema(BaseModel):
    
    time_1: str
    time_2: str
    mercado: str
    odd: str
    
    class Config:
        from_attibutes = True
        
        
        json_schema_extra = {
            "exemplo": {
                "time_1": "Al Hilal Riyadh",
                "time_2": "Al Nassr",
                "mercado": "Mais de 2.5 gols",
                "odd": "3.20"
            }
        }