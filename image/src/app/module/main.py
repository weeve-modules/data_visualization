"""
All logic related to the module's main application
Mostly only this file requires changes
"""
from app.config import APPLICATION
from time import sleep
from app.module.chart import plot_graph
#from app.weeve.egress import send_data

__INPUT_LABEL__ = APPLICATION["INPUT_LABEL"]
__INPUT_UNIT__ = APPLICATION["INPUT_UNIT"]
__SAMPLE_SIZE__ = APPLICATION["SAMPLE_SIZE"]
__INSTANCE_INTERVAL__ = APPLICATION["INSTANCE_INTERVAL"]
__X_AXIS_LABEL__ = APPLICATION["X_AXIS_LABEL"]
__Y_AXIS_LABEL__ = APPLICATION["Y_AXIS_LABEL"]
__GRAPH_TITLE__ = APPLICATION["GRAPH_TITLE"]
__CHART_FILENAME__ = APPLICATION["CHART_FILENAME"]

def module_main(received_data):
    """implement module logic here

    Args:
        parsed_data ([JSON Object]): [Data received by the module and validated by data_validation function]

    Returns:
        [string, string]: [data, error]
    """

    def get_time_data(input_data):
        # change temp and timestamp to 
        return input_data["TIMESTAMP"], input_data[__INPUT_LABEL__]
    try:
        x_axis_data = []
        y_axis_data = []
        count = 0
        if isinstance(received_data, (dict)):
        #  { "TEMPERATUE" : 10, "TIMESTAMP": 103330453 }
            timestamp, data = get_time_data(received_data)
            x_axis_data.append(timestamp)
            y_axis_data.append(data)
            count += 1
            sleep(__INSTANCE_INTERVAL__)
        elif isinstance(received_data, (list)):
        #  [{"TEMPERATUE" : 10,"TIMESTAMP": 103330453 },{},...]
            for item in received_data[::__INSTANCE_INTERVAL__]:
                timestamp, data = get_time_data(item)
                x_axis_data.append(timestamp)
                y_axis_data.append(data)
                count += 1
        if count == __SAMPLE_SIZE__:
            # generate chart
            plot_graph(
                timestamp=x_axis_data,
                data=y_axis_data,
                x_lable=__X_AXIS_LABEL__,
                y_lable= __Y_AXIS_LABEL__,
                graph_title=__GRAPH_TITLE__,
                chart_filename=__CHART_FILENAME__ 
                )

    except Exception:
        return None, "Unable to perform the module logic"
