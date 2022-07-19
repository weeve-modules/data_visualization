"""
All logic related to the module's main application
Mostly only this file requires changes
"""
from time import sleep
from queue import Queue

from app.config import APPLICATION
from app.module.chart import plot_graph


#from app.weeve.egress import send_data

__INPUT_LABEL__ = APPLICATION["INPUT_LABEL"]
__INPUT_UNIT__ = APPLICATION["INPUT_UNIT"]
__SAMPLE_SIZE__ = 10 #APPLICATION["SAMPLE_SIZE"]
__INSTANCE_INTERVAL__ = APPLICATION["INSTANCE_INTERVAL"]
__X_AXIS_LABEL__ = APPLICATION["X_AXIS_LABEL"]
__Y_AXIS_LABEL__ = APPLICATION["Y_AXIS_LABEL"]
__GRAPH_TITLE__ = APPLICATION["GRAPH_TITLE"]
__CHART_FILENAME__ = APPLICATION["CHART_FILENAME"]

x_axis_data = Queue(maxsize=__SAMPLE_SIZE__)
y_axis_data = Queue(maxsize=__SAMPLE_SIZE__)

def module_main(received_data,log):
    """implement module logic here

    Args:
        parsed_data ([JSON Object]): [Data received by the module and validated by data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    
    global x_axis_data
    global y_axis_data

    def get_time_data(input_data):
        # change temp and timestamp to 
        log.info("inside get_time")
        return input_data.get("TIMESTAMP"), input_data.get(__INPUT_LABEL__)
    try:
        if isinstance(received_data, dict):
        #  { "TEMPERATUE" : 10, "TIMESTAMP": 103330453 }
            timestamp, data = get_time_data(received_data)
            log.info(f"timestamp:{timestamp} data: {data}")
            log.info(f"type of timestamp:,{type(timestamp)}")
            log.info(f"type of data:{type(data)}")
            x_axis_data.put(int(timestamp))
            log.info(f"x_axis_data: {x_axis_data}")
            y_axis_data.put(int(data))
            sleep(int(__INSTANCE_INTERVAL__))
        elif isinstance(received_data, list):
        #  [{"TEMPERATUE" : 10,"TIMESTAMP": 103330453 },{},...]
            for item in received_data[::int(__INSTANCE_INTERVAL__)]:
                timestamp, data = get_time_data(item)
                log.info(timestamp, data)
                x_axis_data.put(int(timestamp))
                log.info(f"x_axis_data: {x_axis_data}")
                y_axis_data.put(int(data))
                log.info(f"y_axis_data: {y_axis_data}")
        if x_axis_data.full() and y_axis_data.full(): 
            # generate chart
            x_data = list()
            y_data = list()
            log.info("DOING ALTERATION!!!")
            #log.info(f"x_axis_data: {list(x_axis_data)}\ny_axis_data: {list(y_axis_data)}")

            while not x_axis_data.empty():
                x_data.append(x_axis_data.get())
                log.info(f"NEW x_data:{x_data}")

            while not y_axis_data.empty():
                y_data.append(y_axis_data.get())
                log.info(f"NEW y_data:{y_data}")

            log.info(f"graph plotted for {x_data}, {y_data}")
            plot_graph(
                data=y_data,
                timestamp=x_data,
                x_lable=__X_AXIS_LABEL__,
                y_lable= __Y_AXIS_LABEL__,
                graph_title=__GRAPH_TITLE__,
                chart_filename=__CHART_FILENAME__ 
                )
            

        return None, None

    except Exception as e:
        return None, f"Unable to perform the module logic {e}" 
