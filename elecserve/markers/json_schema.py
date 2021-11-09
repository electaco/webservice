# https://json-schema.org/learn/getting-started-step-by-step

from jsonschema import validate

SCHEMA_POSITION = {
            "type": "object",
            "properties": {
                "X": {"type":"number"},
                "Y": {"type":"number"},
                "Z": {"type":"number"},
            },
            "required": ["X", "Y", "Z"],
        }

SCHEMA_VIDEOSOURCE= {
            "type": "object",
            "properties": {
                "url": {"type":"string"},
                "type": {"type":"string"},
                "ratio": {
                    "type": "array",
                    "items": {"type":"number"},
                    "minItems": 2,
                    "maxItems": 2
                }
            },
            "required": ["url", "type", "ratio"],
        }


SCHEMA_EXTRADATA = {
    "type": "object",
    "required": ["rotation", "source", "scale"],
    "properties": {
        "position": SCHEMA_POSITION,
        "rotation": SCHEMA_POSITION,
        "source": SCHEMA_VIDEOSOURCE,
        "type": {"type":"number"},
        "scale": {"type":"number"},
        "fadeInDistance": {"type":"number"},
        "visibleDistance": {"type":"number"},
    }
}

SCHEMA_MARKER = {
    "type": "object",
    "required": ["id", "name", "position", "type"],
    "properties": {
        "active": {"type":"boolean"},
        "id": {"type":"string"},
        "name": {"type":"string"},
        "type": {"type":"number"},
        "description": {"type":"string"},
        "position": SCHEMA_POSITION
    },
    
}
SCHEMA_MARKERPACK = {
    "type": "object",
    "properties": {
        "active": {"type":"boolean"},
        "icon": {"type":"string"},
        "color": {"type":"string", },
        "id": {"type":"string"},
        "name": {"type":"string"},
        "description": {"type":"string"},
        "markers": {
            "type": "object",
            "patternProperties": {
                "^\d+$": {"type": "array", "items":  SCHEMA_MARKER}
            },
            "additionalProperties": False,
        },
    },
    "required": ["id", "name", "markers"],
}

def validate_markerpack(markerpack):
    return validate(markerpack, SCHEMA_MARKERPACK)