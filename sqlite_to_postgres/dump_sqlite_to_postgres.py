import sqlalchemy

def get_models():
    from app.models import * #this is a syntax warning but just ignore it
    objs = locals()
    models = {}
    for key in objs.keys():
        if not "__" in key:
            models[key] = objs[key]
    return models


