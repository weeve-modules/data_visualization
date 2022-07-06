"""
All constants specific to the application
"""
from app.utils.env import env


APPLICATION = {
    "INPUT_LABEL": env("INPUT_LABEL", "temperature"),
    "INPUT_UNIT": env("INPUT_UNIT", "Celsius"),
    "SAMPLE_SIZE": env("SAMPLE_SIZE", 100),
    "INSTANCE_INTERVAL":env("INSTANCE_INTERVAL",3),
    "X_AXIS_LABEL": env("X_AXIS_LABEL","Sensor Data"),
    "Y_AXIS_LABEL": env("Y_AXIS_LABEL","Timestamp"),
    "GRAPH_TITLE": env("GRAPH_TITLE","Sensor Data Graph"),
    "CHART_FILENAME":env("CHART_FILENAME","graph.png")
}
