#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 16:10:33 2023

@author: mnsgs
"""


import pandas as pd

def export_asset_costs_two_country(my_network):
    '''
    Extracts asset cost results into a csv file for two country case study
    See Network_Structure.csv file in Case Study folder for Asset numbers indexing
    my_network.assets
    '''
    
    costs_df = pd.DataFrame()

    ### RE assets ###
    costs_df.insert(0, 'PV_cost_loc_2_G$', [my_network.assets[12].cost.value])
    costs_df.insert(0, 'PV_cost_loc_1_G$', [my_network.assets[1].cost.value])
    costs_df.insert(0, 'Wind_cost_loc_2_G$', [my_network.assets[13].cost.value])
    costs_df.insert(0, 'Wind_cost_loc_1_G$', [my_network.assets[2].cost.value])
    
    ### PowerPlant CO2 ###
    costs_df.insert(0, 'PP_CO2_loc_2_G$', [my_network.assets[14].cost.value])
    costs_df.insert(0, 'PP_CO2_loc_1_G$', [my_network.assets[3].cost.value])
    
    ### BESS ###
    costs_df.insert(0, 'BESS_loc_2_G$', [my_network.assets[15].cost.value])
    costs_df.insert(0, 'BESS_loc_1_G$', [my_network.assets[4].cost.value])
    
    ### EL to HTH ###
    costs_df.insert(0, 'EL_to_HTH_loc_2_G$', [my_network.assets[16].cost.value])
    costs_df.insert(0, 'EL_to_HTH_loc_1_G$', [my_network.assets[5].cost.value])
    
    ### NH3 to electricity, storage and electricity to NH3 ###
    costs_df.insert(0, 'EL_to_NH3_loc_2_G$', [my_network.assets[17].cost.value])
    costs_df.insert(0, 'EL_to_NH3_loc_1_G$', [my_network.assets[6].cost.value])
    
    costs_df.insert(0, 'NH3_storage_loc_2_G$', [my_network.assets[18].cost.value])
    costs_df.insert(0, 'NH3_storage_loc_1_G$', [my_network.assets[7].cost.value])
    
    costs_df.insert(0, 'NH3_to_EL_loc_2_G$', [my_network.assets[19].cost.value])
    costs_df.insert(0, 'NH3_to_EL_loc_1_G$', [my_network.assets[8].cost.value])
    
    ### NH3 to HTH ###
    costs_df.insert(0, 'NH3_to_HTH_loc_2_G$', [my_network.assets[20].cost.value])
    costs_df.insert(0, 'NH3_to_HTH_loc_1_G$', [my_network.assets[9].cost.value])
    
    ### Transport between locations ###
    costs_df.insert(0, 'HVDC_loc_1-2_G$', [my_network.assets[24].cost.value])
    costs_df.insert(0, 'NH3_transport_loc_1-2_G$', [my_network.assets[23].cost.value])
    
    ### Total cost ### 
    costs_df.insert(0, 'Total_System_Cost', [my_network.problem.value])
    
    return(costs_df)


def export_asset_sizes_two_country(my_network):
    
    sizes_df = pd.DataFrame()

    ### RE assets ###
    sizes_df.insert(0, 'PV_cost_loc_2_GW', [my_network.assets[12].asset_size()])
    sizes_df.insert(0, 'PV_cost_loc_1_GW', [my_network.assets[1].asset_size()])
    sizes_df.insert(0, 'Wind_cost_loc_2_GW', [my_network.assets[13].asset_size()])
    sizes_df.insert(0, 'Wind_cost_loc_1_GW', [my_network.assets[2].asset_size()])
    
    ### PowerPlant CO2 ###
    sizes_df.insert(0, 'PP_CO2_loc_2_GWp', [my_network.assets[14].asset_size()])
    sizes_df.insert(0, 'PP_CO2_loc_1_GWp', [my_network.assets[3].asset_size()])
    
    ### BESS ###
    sizes_df.insert(0, 'BESS_loc_2_GWh', [my_network.assets[15].asset_size()])
    sizes_df.insert(0, 'BESS_loc_1_GWh', [my_network.assets[4].asset_size()])
    
    ### EL to HTH ###
    sizes_df.insert(0, 'EL_to_HTH_loc_2_GWh', [my_network.assets[16].asset_size()])
    sizes_df.insert(0, 'EL_to_HTH_loc_1_GWh', [my_network.assets[5].asset_size()])
    
    ### NH3 to electricity, storage and electricity to NH3 ###
    sizes_df.insert(0, 'EL_to_NH3_loc_2_GWh', [my_network.assets[17].asset_size()])
    sizes_df.insert(0, 'EL_to_NH3_loc_1_GWh', [my_network.assets[6].asset_size()])
    
    sizes_df.insert(0, 'NH3_storage_loc_2_GWh', [my_network.assets[18].asset_size()])
    sizes_df.insert(0, 'NH3_storage_loc_1_GWh', [my_network.assets[7].asset_size()])
    
    sizes_df.insert(0, 'NH3_to_EL_loc_2_GWh', [my_network.assets[19].asset_size()])
    sizes_df.insert(0, 'NH3_to_EL_loc_1_GWh', [my_network.assets[8].asset_size()])
    
    ### NH3 to HTH ###
    sizes_df.insert(0, 'NH3_to_HTH_loc_2_GWh', [my_network.assets[20].asset_size()])
    sizes_df.insert(0, 'NH3_to_HTH_loc_1_GWh', [my_network.assets[9].asset_size()])
    
    ### Transport between locations ###
    sizes_df.insert(0, 'HVDC_loc_1-2_GWp', [my_network.assets[24].asset_size()])
    sizes_df.insert(0, 'NH3_transport_loc_1-2_GWh', [my_network.assets[23].asset_size()])
        
    
    ### Demands ###
    sizes_df.insert(0, 'HTH_demand_loc_2_GWh', [my_network.assets[22].asset_size()])
    sizes_df.insert(0, 'HTH_demand_loc_1_GWh', [my_network.assets[11].asset_size()])
    sizes_df.insert(0, 'EL_demand_loc_2_GWh', [my_network.assets[21].asset_size()])
    sizes_df.insert(0, 'EL_demand_loc_1_GWh', [my_network.assets[10].asset_size()])
    
    ### Emissions ###
    sizes_df.insert(0, 'CO2_Budget_GgCO2', [my_network.assets[0].asset_size()])
    
    return(sizes_df)

def export_asset_costs_two_country_aut(my_network):
    '''
    Extracts asset cost results into a csv file for two country case study
    See Network_Structure.csv file in Case Study folder for Asset numbers indexing
    my_network.assets
    '''
    
    costs_df = pd.DataFrame()

    ### RE assets ###
    costs_df.insert(0, 'PV_cost_loc_2_G$', [my_network.assets[12].cost.value])
    costs_df.insert(0, 'PV_cost_loc_1_G$', [my_network.assets[1].cost.value])
    costs_df.insert(0, 'Wind_cost_loc_2_G$', [my_network.assets[13].cost.value])
    costs_df.insert(0, 'Wind_cost_loc_1_G$', [my_network.assets[2].cost.value])
    
    ### PowerPlant CO2 ###
    costs_df.insert(0, 'PP_CO2_loc_2_G$', [my_network.assets[14].cost.value])
    costs_df.insert(0, 'PP_CO2_loc_1_G$', [my_network.assets[3].cost.value])
    
    ### BESS ###
    costs_df.insert(0, 'BESS_loc_2_G$', [my_network.assets[15].cost.value])
    costs_df.insert(0, 'BESS_loc_1_G$', [my_network.assets[4].cost.value])
    
    ### EL to HTH ###
    costs_df.insert(0, 'EL_to_HTH_loc_2_G$', [my_network.assets[16].cost.value])
    costs_df.insert(0, 'EL_to_HTH_loc_1_G$', [my_network.assets[5].cost.value])
    
    ### NH3 to electricity, storage and electricity to NH3 ###
    costs_df.insert(0, 'EL_to_NH3_loc_2_G$', [my_network.assets[17].cost.value])
    costs_df.insert(0, 'EL_to_NH3_loc_1_G$', [my_network.assets[6].cost.value])
    
    costs_df.insert(0, 'NH3_storage_loc_2_G$', [my_network.assets[18].cost.value])
    costs_df.insert(0, 'NH3_storage_loc_1_G$', [my_network.assets[7].cost.value])
    
    costs_df.insert(0, 'NH3_to_EL_loc_2_G$', [my_network.assets[19].cost.value])
    costs_df.insert(0, 'NH3_to_EL_loc_1_G$', [my_network.assets[8].cost.value])
    
    ### NH3 to HTH ###
    costs_df.insert(0, 'NH3_to_HTH_loc_2_G$', [my_network.assets[20].cost.value])
    costs_df.insert(0, 'NH3_to_HTH_loc_1_G$', [my_network.assets[9].cost.value])
    
    ### Total cost ### 
    costs_df.insert(0, 'Total_System_Cost', [my_network.problem.value])
    
    return(costs_df)


def export_asset_sizes_two_country_aut(my_network):
    
    sizes_df = pd.DataFrame()

    ### RE assets ###
    sizes_df.insert(0, 'PV_cost_loc_2_GW', [my_network.assets[12].asset_size()])
    sizes_df.insert(0, 'PV_cost_loc_1_GW', [my_network.assets[1].asset_size()])
    sizes_df.insert(0, 'Wind_cost_loc_2_GW', [my_network.assets[13].asset_size()])
    sizes_df.insert(0, 'Wind_cost_loc_1_GW', [my_network.assets[2].asset_size()])
    
    ### PowerPlant CO2 ###
    sizes_df.insert(0, 'PP_CO2_loc_2_GWp', [my_network.assets[14].asset_size()])
    sizes_df.insert(0, 'PP_CO2_loc_1_GWp', [my_network.assets[3].asset_size()])
    
    ### BESS ###
    sizes_df.insert(0, 'BESS_loc_2_GWh', [my_network.assets[15].asset_size()])
    sizes_df.insert(0, 'BESS_loc_1_GWh', [my_network.assets[4].asset_size()])
    
    ### EL to HTH ###
    sizes_df.insert(0, 'EL_to_HTH_loc_2_GWh', [my_network.assets[16].asset_size()])
    sizes_df.insert(0, 'EL_to_HTH_loc_1_GWh', [my_network.assets[5].asset_size()])
    
    ### NH3 to electricity, storage and electricity to NH3 ###
    sizes_df.insert(0, 'EL_to_NH3_loc_2_GWh', [my_network.assets[17].asset_size()])
    sizes_df.insert(0, 'EL_to_NH3_loc_1_GWh', [my_network.assets[6].asset_size()])
    
    sizes_df.insert(0, 'NH3_storage_loc_2_GWh', [my_network.assets[18].asset_size()])
    sizes_df.insert(0, 'NH3_storage_loc_1_GWh', [my_network.assets[7].asset_size()])
    
    sizes_df.insert(0, 'NH3_to_EL_loc_2_GWh', [my_network.assets[19].asset_size()])
    sizes_df.insert(0, 'NH3_to_EL_loc_1_GWh', [my_network.assets[8].asset_size()])
    
    ### NH3 to HTH ###
    sizes_df.insert(0, 'NH3_to_HTH_loc_2_GWh', [my_network.assets[20].asset_size()])
    sizes_df.insert(0, 'NH3_to_HTH_loc_1_GWh', [my_network.assets[9].asset_size()])
        
    
    ### Demands ###
    sizes_df.insert(0, 'HTH_demand_loc_2_GWh', [my_network.assets[22].asset_size()])
    sizes_df.insert(0, 'HTH_demand_loc_1_GWh', [my_network.assets[11].asset_size()])
    sizes_df.insert(0, 'EL_demand_loc_2_GWh', [my_network.assets[21].asset_size()])
    sizes_df.insert(0, 'EL_demand_loc_1_GWh', [my_network.assets[10].asset_size()])
    
    ### Emissions ###
    sizes_df.insert(0, 'CO2_Budget_GgCO2', [my_network.assets[0].asset_size()])
    
    return(sizes_df)