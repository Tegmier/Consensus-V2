import numpy as np
import pandas as pd
import os
from datetime import datetime
from utils.data_preparation_toolkit import (create_security_revenue_data, 
                                           create_security_revenue_data_consecutive_beat,
                                           create_security_revenue_data_beat_analysis)
from utils.data_visualiztion_toolkit import (path_check,
                                             output_beat_miss_statistical_feature, 
                                             plot_alpha_figure, 
                                             output_beat_miss_beta, 
                                             plot_alpha_beatmiss_ratio_figure,plot_stock_price, 
                                             report_overall_feature_cross_region_sector,
                                             plot_retrace_distribution,
                                             report_retrace_statistics,
                                             plot_retrace_beatsize,
                                             security_revenue_data_to_xlsx,
                                             beat_analysis_data_to_xlsx
                                             )
from utils.data_process_toolkit import calculate_excess_return, calculate_stock_return
import matplotlib.pyplot as plt
import shutup

shutup.please()
# parameters

path = "data/spx"
sector = "SPX"
for equity in os.listdir(path):
    data = pd.read_excel(os.path.join(path, equity), engine="openpyxl")
    if "P/E" not in data.columns:
        print(equity)