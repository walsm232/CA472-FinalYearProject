import uuid

def Get_Random_Identifier():
    random_ID = str(uuid.uuid4())[:8].replace('-', '').lower()
    return random_ID