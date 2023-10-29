#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:28:01 2023

@author: mnsgs
"""

import pandas as pd

def export_asset_costs(my_network):
    costs_df = pd.DataFrame()

    ### RE assets ###
    costs_df.insert(0, 'PVRoof_cost_G$', [my_network.assets[1].cost.value])
    costs_df.insert(0, 'PVOpen_cost_G$', [my_network.assets[2].cost.value])
    costs_df.insert(0, 'WindOnsh_cost_G$', [my_network.assets[3].cost.value])
    costs_df.insert(0, 'WindOffsh_cost_G$', [my_network.assets[4].cost.value])
   
    
    ### BESS ###
    costs_df.insert(0, 'BESS_G$', [my_network.assets[6].cost.value])

    
    ### NH3 to electricity, storage and electricity to NH3 ###
    costs_df.insert(0, 'NH3_to_EL_G$', [my_network.assets[10].cost.value])
    costs_df.insert(0, 'NH3_storage_G$', [my_network.assets[9].cost.value])
    costs_df.insert(0, 'EL_to_NH3_G$', [my_network.assets[8].cost.value])
    
    ### NH3 to HTH ###
    costs_df.insert(0, 'NH3_to_HTH_G$', [my_network.assets[11].cost.value])
    
    
    ### EL to HTH ###
    costs_df.insert(0, 'EL_to_HTH_G$', [my_network.assets[7].cost.value])
    
    
    ### PowerPlant CO2 ###
    costs_df.insert(0, 'PP_CO2_G$', [my_network.assets[5].cost.value])
    
    ### Demands ###
    costs_df.insert(0, 'HTH_demand_G$', [my_network.assets[13].cost.value])
    costs_df.insert(0, 'EL_demand_G$', [my_network.assets[12].cost.value])
    
    ### Total cost ### 
    costs_df.insert(0, 'Total_System_Cost', [my_network.problem.value])
    
    return(costs_df)


def export_asset_sizes(my_network):
    
    sizes_df = pd.DataFrame()

    ### RE assets ###
    sizes_df.insert(0, 'PVRoof_size_GWp', [my_network.assets[1].asset_size()])
    sizes_df.insert(0, 'PVOpen_size_GWp', [my_network.assets[2].asset_size()])
    sizes_df.insert(0, 'WindOnsh_size_GWp', [my_network.assets[3].asset_size()])
    sizes_df.insert(0, 'WindOffsh_size_GWp', [my_network.assets[4].asset_size()])
    
    ### BESS ###
    sizes_df.insert(0, 'BESS_GWh', [my_network.assets[6].asset_size()])
    
    ### NH3 to electricity, storage and electricity to NH3 ###
    sizes_df.insert(0, 'NH3_to_EL_GW', [my_network.assets[10].asset_size()])
    sizes_df.insert(0, 'NH3_storage_GWh', [my_network.assets[9].asset_size()])
    sizes_df.insert(0, 'EL_to_NH3_GW', [my_network.assets[8].asset_size()])
    
    ### NH3 to HTH ###
    sizes_df.insert(0, 'NH3_to_HTH_GW', [my_network.assets[11].asset_size()])
    
    
    ### EL to HTH ###
    sizes_df.insert(0, 'EL_to_HTH_GW', [my_network.assets[7].asset_size()])
    
    
    ### PowerPlant CO2 ###
    sizes_df.insert(0, 'PP_CO2_GW', [my_network.assets[5].asset_size()])
    
    ### Demands ###
    sizes_df.insert(0, 'HTH_demand_GWh', [my_network.assets[13].asset_size()])
    sizes_df.insert(0, 'EL_demand_GWh', [my_network.assets[12].asset_size()])
    
    ### Emissions ###
    sizes_df.insert(0, 'CO2_Budget_GgCO2e', [my_network.assets[0].asset_size()])
    
    return(sizes_df)