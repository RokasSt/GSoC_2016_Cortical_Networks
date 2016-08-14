##########################################################################################################################
###    This script was developed as part of GSoC 2016 project on Cortical Network Development          ###################
##     Author : Rokas Stanislovas                                            #############################################
##########################################################################################################################

import opencortex
import opencortex.build as oc
import opencortex.utils as oc_utils
import neuroml
import random

opencortex.print_comment_v("Using OpenCortex to convert Potjans2014 interface to NeuroML2")

def RunPotjans2014(net_id='TestRunPotjans2014',
                   neuron_params = {'cm'        : 0.25,  # nF
                                    'i_offset'  : 0.0,   # nA
                                    'tau_m'     : 10.0,  # ms
                                    'tau_refrac': 2.0,   # ms
                                    'tau_syn_E' : 0.5,   # ms
                                    'tau_syn_I' : 0.5,   # ms
                                    'v_reset'   : -65.0,  # mV
                                    'v_rest'    : -65.0,  # mV         
                                    'v_thresh'  : -50.0,  # mV 
                                    'v_init'    : -58.0  # mV
                                    },
                   V0_mean = -58.0,
                   V0_sd= 5.0,
                   which_populations='all',
                   scale_excitatory_cortex=0.01,
                   scale_inhibitory_cortex=0.01,
                   scale_thalamus=0.01,  
                   input_scaling=1.0,
                   rel_inh_syn_w=-4.0,
                   input_type='poisson',
                   thalamic_input=False,
                   duration=300,
                   dt=0.025,
                   max_memory='4000M',
                   seed=1234,
                   simulator=None):
                   
    nml_doc, network = oc.generate_network(net_id,seed)
                   
    popDictFull={}
                   
    ##############   Full model ##################################
    
    popDictFull['L23_E'] = (20683, 'L23','IF_curr_exp_L23_E','single')
    popDictFull['L23_I'] = (5834, 'L23','IF_curr_exp_L23_I','single')
    popDictFull['L4_E'] = (21915, 'L4','IF_curr_exp_L4_E','single')
    popDictFull['L4_I'] = (5479, 'L4','IF_curr_exp_L4_I','single')
    popDictFull['L5_E']= (4850,'L5','IF_curr_exp_L5_E','single')          
    popDictFull['L5_I']= (1065,'L5','IF_curr_exp_L5_I','single')
    popDictFull['L6_E']= (14395,'L23','IF_curr_exp_L6_E','single')
    popDictFull['L6_I']= (2948,'L6','IF_curr_exp_L6_I','single')
    
    popDictFull['Thalamus_E']=(902,'Thalamus')
    
    ###############################################################
    
    popDict={}
    
    if thalamic_input:
    
       scaledThalamus={}
    
    for cell_pop_id in popDictFull.keys():
        
        if which_populations=='all' or cell_pop_id in which_populations:
           
           if 'Thalamus' not in cell_pop_id:
           
              popDict[cell_pop_id]=()
           
              if 'E' in cell_pop_id:
             
                 popDict[cell_pop_id]=(int(round(scale_excitatory_cortex*popDictFull[cell_pop_id][0])), 
                                       popDictFull[cell_pop_id][1],
                                       popDictFull[cell_pop_id][2],
                                       popDictFull[cell_pop_id][3])
             
              if 'I' in cell_pop_id:
                  
                 popDict[cell_pop_id]=(int(round(scale_inhibitory_cortex*popDictFull[cell_pop_id][0])), 
                                       popDictFull[cell_pop_id][1],
                                       popDictFull[cell_pop_id][2],
                                       popDictFull[cell_pop_id][3])
               
           else:
           
              if thalamic_input:
             
                 scaledThalamus[cell_pop_id]=( int(round(scale_thalamus*popDictFull[cell_pop_id][0])),popDictFull[cell_pop_id][1])
                 
    popDictFinal={}
    
    for cell_pop_id in popDict.keys():
    
        if V0_mean != None and  V0_sd != None:

           for cell_ind in range(0,popDict[cell_pop_id][0]):
           
               v0=random.gauss(V0_mean,V0_sd)
               
               new_pop_id=cell_pop_id+str(cell_ind)
           
               PyNN_cell=neuroml.IF_curr_exp(id=popDict[cell_pop_id][2]+str(cell_ind),
                                             cm=neuron_params['cm'],
                                             i_offset=neuron_params['i_offset'],
                                             tau_syn_E=neuron_params['tau_syn_E'], 
                                             tau_syn_I=neuron_params['tau_syn_I'], 
                                             v_init=v0, 
                                             tau_m=neuron_params['tau_m'], 
                                             tau_refrac=neuron_params['tau_refrac'], 
                                             v_reset=neuron_params['v_reset'], 
                                             v_rest=neuron_params['v_rest'], 
                                             v_thresh=neuron_params['v_thresh'])
                                             
               nml_doc.IF_curr_exp.append(PyNN_cell)
               
               popDictFinal[new_pop_id]=(1,popDict[cell_pop_id][1],popDict[cell_pop_id][2]+str(cell_ind))
            
        else:
        
           popDictFinal[cell_pop_id]=popDict[cell_pop_id]
           
           PyNN_cell=neuroml.IF_curr_exp(id=popDict[cell_pop_id][2],
                                         cm=neuron_params['cm'],
                                         i_offset=neuron_params['i_offset'],
                                         tau_syn_E=neuron_params['tau_syn_E'], 
                                         tau_syn_I=neuron_params['tau_syn_I'], 
                                         v_init=neuron_params['v_init'], 
                                         tau_m=neuron_params['tau_m'], 
                                         tau_refrac=neuron_params['tau_refrac'], 
                                         v_reset=neuron_params['v_reset'], 
                                         v_rest=neuron_params['v_rest'], 
                                         v_thresh=neuron_params['v_thresh'])
                                             
           nml_doc.IF_curr_exp.append(PyNN_cell)
           
    t1=-100
    t2=-150
    t3=-150
    t4=-300.0
    t5=-300.0
    t6=-300.0
    t7=-200.0
    t8=-200.0

    boundaries={}

    boundaries['L1']=[0,t1]
    boundaries['L23']=[t1,t1+t2+t3]
    boundaries['L4']=[t1+t2+t3,t1+t2+t3+t4]
    boundaries['L5']=[t1+t2+t3+t4,t1+t2+t3+t4+t5]
    boundaries['L6']=[t1+t2+t3+t4+t5,t1+t2+t3+t4+t5+t6]
    boundaries['Thalamus']=[t1+t2+t3+t4+t5+t6+t7,t1+t2+t3+t4+t5+t6+t7+t8]
    
    xs = [0,1000]
    zs = [0,1000] 
    
    passed_pops=oc_utils.check_pop_dict_and_layers(pop_dict=popDictFinal,boundary_dict=boundaries)
    
    if passed_pops:
    
       opencortex.print_comment_v("Population parameters were specified correctly.") 
       
       #other options
      
       pop_params=oc_utils.add_populations_in_cylindrical_layers(network,boundaries,popDictFinal,radiusOfCylinder=500,numOfSides=6)
       
       #pop_params=oc_utils.add_populations_in_cylindrical_layers(network,boundaries,popDictFinal,radiusOfCylinder=500)
                                                                 
       #pop_params=oc_utils.add_populations_in_rectangular_layers(network,boundaries,popDictFinal,xs,zs) 
       
    else:
    
       opencortex.print_comment_v("Population parameters were specified incorrectly; execution of RunPotjans2014.py will terminate.")
       
       quit() 
    
    pop_tags_on_matrix=['L23_E','L23_I','L4_E','L4_I', 'L5_E','L5_I', 'L6_E','L6_I']
    
    # Probabilities for >=1 connection between neurons in the given populations. 
    # The first index is for the target population; the second for the source population
    #             2/3e      2/3i    4e      4i      5e      5i      6e      6i
    conn_probs = [[0.1009,  0.1689, 0.0437, 0.0818, 0.0323, 0.,     0.0076, 0.    ],
                 [0.1346,   0.1371, 0.0316, 0.0515, 0.0755, 0.,     0.0042, 0.    ],
                 [0.0077,   0.0059, 0.0497, 0.135,  0.0067, 0.0003, 0.0453, 0.    ],
                 [0.0691,   0.0029, 0.0794, 0.1597, 0.0033, 0.,     0.1057, 0.    ],
                 [0.1004,   0.0622, 0.0505, 0.0057, 0.0831, 0.3726, 0.0204, 0.    ],
                 [0.0548,   0.0269, 0.0257, 0.0022, 0.06,   0.3158, 0.0086, 0.    ],
                 [0.0156,   0.0066, 0.0211, 0.0166, 0.0572, 0.0197, 0.0396, 0.2252],
                 [0.0364,   0.001,  0.0034, 0.0005, 0.0277, 0.008,  0.0658, 0.1443]]
                 
    conn_mean_w=[[87.8E-3,  rel_inh_syn_w*87.8E-3, 2*87.8E-3, rel_inh_syn_w*2*87.8E-3, 87.8E-3, rel_inh_syn_w*87.8E-3, 87.8E-3, rel_inh_syn_w*87.8E-3],
                    [87.8E-3,  rel_inh_syn_w*87.8E-3,   87.8E-3,   rel_inh_syn_w*87.8E-3, 87.8E-3, rel_inh_syn_w*87.8E-3, 87.8E-3, rel_inh_syn_w*87.8E-3],
                    [87.8E-3,  rel_inh_syn_w*87.8E-3,   87.8E-3,   rel_inh_syn_w*87.8E-3, 87.8E-3, rel_inh_syn_w*87.8E-3, 87.8E-3, rel_inh_syn_w*87.8E-3],
                    [87.8E-3,  rel_inh_syn_w*87.8E-3,   87.8E-3,   rel_inh_syn_w*87.8E-3, 87.8E-3, rel_inh_syn_w*87.8E-3, 87.8E-3, rel_inh_syn_w*87.8E-3],
                    [87.8E-3,  rel_inh_syn_w*87.8E-3,   87.8E-3,   rel_inh_syn_w*87.8E-3, 87.8E-3, rel_inh_syn_w*87.8E-3, 87.8E-3, rel_inh_syn_w*87.8E-3],
                    [87.8E-3,  rel_inh_syn_w*87.8E-3,   87.8E-3,   rel_inh_syn_w*87.8E-3, 87.8E-3, rel_inh_syn_w*87.8E-3, 87.8E-3, rel_inh_syn_w*87.8E-3],
                    [87.8E-3,  rel_inh_syn_w*87.8E-3,   87.8E-3,   rel_inh_syn_w*87.8E-3, 87.8E-3, rel_inh_syn_w*87.8E-3, 87.8E-3, rel_inh_syn_w*87.8E-3],
                    [87.8E-3,  rel_inh_syn_w*87.8E-3,   87.8E-3,   rel_inh_syn_w*87.8E-3, 87.8E-3, rel_inh_syn_w*87.8E-3, 87.8E-3, rel_inh_syn_w*87.8E-3]]  
                 
    conn_std_w=[[0.1,  0.1, 0.05, 0.1, 0.1, 0.1, 0.1, 0.1],
                [0.1,  0.1,  0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
                [0.1,  0.1,  0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
                [0.1,  0.1,  0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
                [0.1,  0.1,  0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
                [0.1,  0.1,  0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
                [0.1,  0.1,  0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
                [0.1,  0.1,  0.1, 0.1, 0.1, 0.1, 0.1, 0.1]] 
                
    conn_mean_delay=[[1.5,  0.75, 1.5, 0.75, 1.5, 0.75, 1.5, 0.75],
                     [1.5,  0.75, 1.5, 0.75, 1.5, 0.75, 1.5, 0.75],
                     [1.5,  0.75, 1.5, 0.75, 1.5, 0.75, 1.5, 0.75],
                     [1.5,  0.75, 1.5, 0.75, 1.5, 0.75, 1.5, 0.75],
                     [1.5,  0.75, 1.5, 0.75, 1.5, 0.75, 1.5, 0.75],
                     [1.5,  0.75, 1.5, 0.75, 1.5, 0.75, 1.5, 0.75],
                     [1.5,  0.75, 1.5, 0.75, 1.5, 0.75, 1.5, 0.75],
                     [1.5,  0.75, 1.5, 0.75, 1.5, 0.75, 1.5, 0.75]] 
                         
    conn_std_delay=[[0.75,  0.375, 0.75, 0.375, 0.75, 0.375, 0.75, 0.375],
                    [0.75,  0.375, 0.75, 0.375, 0.75, 0.375, 0.75, 0.375],
                    [0.75,  0.375, 0.75, 0.375, 0.75, 0.375, 0.75, 0.375],
                    [0.75,  0.375, 0.75, 0.375, 0.75, 0.375, 0.75, 0.375],
                    [0.75,  0.375, 0.75, 0.375, 0.75, 0.375, 0.75, 0.375],
                    [0.75,  0.375, 0.75, 0.375, 0.75, 0.375, 0.75, 0.375],
                    [0.75,  0.375, 0.75, 0.375, 0.75, 0.375, 0.75, 0.375],
                    [0.75,  0.375, 0.75, 0.375, 0.75, 0.375, 0.75, 0.375]] 
                    
    syn=neuroml.ExpCurrSynapse(id='exp_curr_syn_all',tau_syn=0.5)
    
    nml_doc.exp_curr_synapses.append(syn)
                    
    syn_id_matrix=[['exp_curr_syn_all']]       # utils method build_probability_based_connectivity will assume that the same synapse model is shared by all projections; 
                                               # however, it must be inside 'list' because generically each physical projection might contain multiple synaptic components.
                 
    # In-degrees for external inputs
    
    K_ext = {
    'L23': {'E': 1600, 'I': 1500},
    'L4' : {'E': 2100, 'I': 1900},
    'L5' : {'E': 2000, 'I': 1900},
    'L6' : {'E': 2900, 'I': 2100}
    }
    
    input_params ={'L23_E':[{'InputType':'GeneratePoissonTrains',
                             'InputName':"EXT_L23_E",
                             'TrainType':'persistent',
                             'Synapse':'exp_curr_syn_all',
                             'AverageRateList':[8.0],
                             'RateUnits':'Hz',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1600} },
                             
                            {'InputType':'PulseGenerators',
                             'InputName':"Ext_L23_E",
                             'Noise':False,
                             'AmplitudeList':[],
                             'DurationList':[],
                             'DelayList':[],
                             'TimeUnits':'ms',
                             'AmplitudeUnits':'nA',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1600}  }],
                     
                   'L23_I':[{'InputType':'GeneratePoissonTrains',
                             'InputName':"EXT_L23_I",
                             'TrainType':'persistent',
                             'Synapse':'exp_curr_syn_all',
                             'AverageRateList':[8.0],
                             'RateUnits':'Hz',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1500} },
                             
                            {'InputType':'PulseGenerators',
                             'InputName':"Ext_L23_I",
                             'Noise':False,
                             'AmplitudeList':[],
                             'DurationList':[],
                             'DelayList':[],
                             'TimeUnits':'ms',
                             'AmplitudeUnits':'nA',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1500}  }],
                     
                   'L4_E':[ {'InputType':'GeneratePoissonTrains',
                             'InputName':"EXT_L4_E",
                             'TrainType':'persistent',
                             'Synapse':'exp_curr_syn_all',
                             'AverageRateList':[8.0],
                             'RateUnits':'Hz',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:2100} },
                             
                            {'InputType':'PulseGenerators',
                             'InputName':"Ext_L4_E",
                             'Noise':False,
                             'AmplitudeList':[],
                             'DurationList':[],
                             'DelayList':[],
                             'TimeUnits':'ms',
                             'AmplitudeUnits':'nA',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1600}  }], 
                     
                   'L4_I':[ {'InputType':'GeneratePoissonTrains',
                             'InputName':"EXT_L4_I",
                             'TrainType':'persistent',
                             'Synapse':'exp_curr_syn_all',
                             'AverageRateList':[8.0],
                             'RateUnits':'Hz',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1900}},
                             
                            {'InputType':'PulseGenerators',
                             'InputName':"Ext_L4_I",
                             'Noise':False,
                             'AmplitudeList':[],
                             'DurationList':[],
                             'DelayList':[],
                             'TimeUnits':'ms',
                             'AmplitudeUnits':'nA',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1600}  } ],
                     
                   'L5_E':[ {'InputType':'GeneratePoissonTrains',
                             'InputName':"EXT_L5_E",
                             'TrainType':'persistent',
                             'Synapse':'exp_curr_syn_all',
                             'AverageRateList':[8.0],
                             'RateUnits':'Hz',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:2000}},
                             
                            {'InputType':'PulseGenerators',
                             'InputName':"Ext_L5_E",
                             'Noise':False,
                             'AmplitudeList':[],
                             'DurationList':[],
                             'DelayList':[],
                             'TimeUnits':'ms',
                             'AmplitudeUnits':'nA',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1600}  } ],
                             
                   'L5_I':[ {'InputType':'GeneratePoissonTrains',
                             'InputName':"EXT_L5_I",
                             'TrainType':'persistent',
                             'Synapse':'exp_curr_syn_all',
                             'AverageRateList':[8.0],
                             'RateUnits':'Hz',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1900}},
                             
                            {'InputType':'PulseGenerators',
                             'InputName':"Ext_L5_I",
                             'Noise':False,
                             'AmplitudeList':[],
                             'DurationList':[],
                             'DelayList':[],
                             'TimeUnits':'ms',
                             'AmplitudeUnits':'nA',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1600}  } ],
                     
                   'L6_E':[ {'InputType':'GeneratePoissonTrains',
                             'InputName':"EXT_L6_E",
                             'TrainType':'persistent',
                             'Synapse':'exp_curr_syn_all',
                             'AverageRateList':[8.0],
                             'RateUnits':'Hz',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:2900}},
                             
                            {'InputType':'PulseGenerators',
                             'InputName':"Ext_L6_E",
                             'Noise':False,
                             'AmplitudeList':[],
                             'DurationList':[],
                             'DelayList':[],
                             'TimeUnits':'ms',
                             'AmplitudeUnits':'nA',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1600}  } ],    
                             
                   'L6_I':[ {'InputType':'GeneratePoissonTrains',
                             'InputName':"EXT_L6_I",
                             'TrainType':'persistent',
                             'Synapse':'exp_curr_syn_all',
                             'AverageRateList':[8.0],
                             'RateUnits':'Hz',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:2100}},
                             
                            {'InputType':'PulseGenerators',
                             'InputName':"Ext_L6_I",
                             'Noise':False,
                             'AmplitudeList':[],
                             'DurationList':[],
                             'DelayList':[],
                             'TimeUnits':'ms',
                             'AmplitudeUnits':'nA',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1600}  } ] }
                             
    for pop_id in input_params.keys(): 
    
        for input_group_ind in range(0,len(input_params[pop_id]) ):
           
            if input_type=='poisson' and input_params[pop_id][input_group_ind]['InputType']=='PulseGenerators':
            
               del input_params[pop_id][input_group_ind]
                   
    if input_scaling != 1.0:              
                   
       for pop_id in input_params.keys(): 
    
           for input_group_ind in range(0,len(input_params[pop_id]) ):
           
               if 'TargetDict' in input_params[pop_id][input_group_ind].keys():
               
                  if None in input_params[pop_id][input_group_ind]['TargetDict'].keys():
                      
                     num_of_inputs_per_cell=int(round(input_params[pop_id][input_group_ind]['TargetDict'][None]*input_scaling) )
                      
                     if num_of_inputs_per_cell !=0:
                      
                        input_params[pop_id][input_group_ind]['TargetDict'][None]=num_of_inputs_per_cell
                         
                        for pop_tag_ind in range(0,len(pop_tags_on_matrix)):
                         
                            if pop_tags_on_matrix[pop_tag_ind] == pop_id:
                             
                               post_pop_tag=pop_tag_ind
                                
                               for post_pop_index in range(0,len(conn_mean_w)):
                                
                                   if post_pop_tag == post_pop_index:
                                
                                      for pre_pop_index in range(0,len(conn_mean_w[post_pop_index])):
                                       
                                          conn_mean_w[post_pop_index][pre_pop_index]=(1.0/math.sqrt(num_of_inputs_per_cell))*conn_mean_w[post_pop_index][pre_pop_index]
                                          
                                          conn_std_w[post_pop_index][pre_pop_index]=(1.0/math.sqrt(num_of_inputs_per_cell))*conn_std_w[post_pop_index][pre_pop_index]
                                                                   
                     else:
                      
                        del input_params[pop_id][input_group_ind]   
                         
                        if input_params[pop_id] == []:
                         
                           del input_params[pop_id] 
          
    proj_array=oc_utils.build_probability_based_connectivity(net=network,
                                                             pop_params=pop_params,
                                                             probability_matrix=conn_probs, 
                                                             synapse_matrix=syn_id_matrix,
                                                             weight_matrix=conn_mean_w, 
                                                             delay_matrix=conn_mean_delay,
                                                             tags_on_populations=pop_tags_on_matrix, 
                                                             std_weight_matrix=conn_std_w,
                                                             std_delay_matrix=conn_std_delay)
                                                             
    input_list_array_final, input_synapse_list=oc_utils.build_inputs(nml_doc=nml_doc,
                                                                     net=network,
                                                                     population_params=pop_params,
                                                                     input_params=input_params,
                                                                     cached_dicts=None,
                                                                     path_to_cells=None,
                                                                     path_to_synapses=False)
                                                                     
    # Mean rates in the full-scale model, necessary for scaling
    # Precise values differ somewhat between network realizations
    
    full_mean_rates = {
    'L23': {'E': 0.971, 'I': 2.868},
    'L4' : {'E': 4.746, 'I': 5.396},
    'L5' : {'E': 8.142, 'I': 9.078},
    'L6' : {'E': 0.991, 'I': 7.523}

    }                                                                 
    
    # Background rate per synapse: done
    # bg_rate = 8.  # spikes/s
    
    # Parameters for transient thalamic input
    thalamic_input = False
    thal_params = {
    # Number of neurons in thalamic population
    'n_thal'      : 902,
    # Connection probabilities
    'C'           : {'L23': {'E': 0, 'I': 0},
                   'L4' : {'E': 0.0983, 'I': 0.0619},
                   'L5' : {'E': 0, 'I': 0},
                   'L6' : {'E': 0.0512, 'I': 0.0196}},
    'rate'        : 120.,  # spikes/s;
    'start'       : 700.,  # ms
    'duration'    : 10.   # ms;
    }

    # Plotting parameters
    #create_raster_plot = True
    #raster_t_min = 0  # ms
    #raster_t_max = sim_params.simulator_params[simulator]['sim_duration']  # ms
    # Fraction of recorded neurons to include in raster plot
    #frac_to_plot = 0.01
    #'N_scaling' : 1.,
    # Fraction of in-degrees to simulate. Upon downscaling, synaptic weights are 
    # taken proportional to 1/sqrt(in-degree) and external drive is adjusted 
    # to preserve mean and variances of activity in the diffusion approximation.
    # In-degrees and weights of both intrinsic and extrinsic inputs are adjusted.
    # This scaling was not part of the original study, but this option is included
    # here to enable simulations on small systems that give results similar to
    # full-scale simulations.
    # 'K_scaling' 0.5,
    # Type of background input. Possible values: 'poisson' or 'DC'
    # If 'DC' is chosen, a constant external current is provided, equal to the mean 
    # current due to the Poisson input used in the default version of the model.
    #'input_type' : 'poisson',
    # Whether to record from a fixed fraction of neurons in each population. 
    # If False, a fixed number of neurons is recorded.
    
    nml_file_name = '%s.net.nml'%network.id
    
    oc.save_network(nml_doc, nml_file_name, validate=True,max_memory=max_memory)
    
    lems_file_name=oc.generate_lems_simulation(nml_doc, 
                                               network, 
                                               nml_file_name, 
                                               duration =duration, 
                                               dt =dt)
     
    if simulator != None:                                          
                                               
       opencortex.print_comment_v("Starting simulation of %s.net.nml"%net_id)
                            
       oc.simulate_network(lems_file_name=lems_file_name,
                           simulator=simulator,
                           max_memory=max_memory)
    
    
if __name__=="__main__":

   ## generation is faster when initial membrane potential does not vary with the cell instance
   RunPotjans2014(V0_mean = None,V0_sd= None)
   
   #RunPotjans2014()
