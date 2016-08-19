##########################################################################################################################
###    This script was developed as part of GSoC 2016 project on Cortical Network Development          ###################
##     Author : Rokas Stanislovas                                            #############################################
##########################################################################################################################
#### Converting https://github.com/NeuralEnsemble/PyNN/tree/master/examples/Potjans2014 to NeuroML2 using OpenCortex API##

import opencortex
import opencortex.build as oc
import opencortex.utils as oc_utils
import neuroml
import random
import numpy as np

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
                   bg_rate=8.0,       # spikes/s
                   w_mean = 87.8e-3, # nA
                   w_ext = 87.8e-3, # nA
                   w_234 = 2 * 87.8e-3,  # nA
                   w_rel = 0.1,
                   w_rel_234 = 0.05,
                   d_mean = {'E': 1.5, 'I': 0.75},
                   d_sd = {'E': 0.75, 'I': 0.375},
                   K_ext = {'L23_E': 1600, 
                            'L23_I': 1500,
                            'L4_E': 2100, 
                            'L4_I': 1900,
                            'L5_E': 2000, 
                            'L5_I': 1900,
                            'L6_E': 2900, 
                            'L6_I': 2100},
                   full_mean_rates = {'L23_E': 0.971, 
                                      'L23_I': 2.868,
                                      'L4_E': 4.746, 
                                      'L4_I': 5.396,
                                      'L5_E': 8.142, 
                                      'L5_I': 9.078,
                                      'L6_E' : 0.991, 
                                      'L6_I': 7.523},
                   thal_params = {
                   # Number of neurons in thalamic population
                   'n_thal'      : 902,
                   # Connection probabilities
                   'C'           : {'L23_E': 0,
                                    'L23_I': 0,
                                    'L4_E' : 0.0983, 
                                    'L4_I': 0.0619,
                                    'L5_E' : 0, 
                                    'L5_I': 0,
                                    'L6_E' : 0.0512, 
                                    'L6_I': 0.0196},
                   'rate'        : 120.,  # spikes/s;
                   'start'       : 700.,  # ms
                   'duration'    : 10.   # ms;
                   },
                   which_populations='all',
                   scale_excitatory_cortex=0.01,
                   scale_inhibitory_cortex=0.01,
                   scale_thalamus=0.01,  
                   K_scaling=1.0,
                   rel_inh_syn_w=-4.0,
                   input_type='poisson',
                   thalamic_input=False,
                   duration=300,
                   dt=0.025,
                   max_memory='4000M',
                   seed=1234,
                   simulator=None):
    
    ######################### Full-scale model #############################################################
    
    popDictFull={}
    
    popDictFull['L23_E'] = (20683, 'L23','IF_curr_exp_L23_E','single')
    popDictFull['L23_I'] = (5834, 'L23','IF_curr_exp_L23_I','single')
    popDictFull['L4_E'] = (21915, 'L4','IF_curr_exp_L4_E','single')
    popDictFull['L4_I'] = (5479, 'L4','IF_curr_exp_L4_I','single')
    popDictFull['L5_E']= (4850,'L5','IF_curr_exp_L5_E','single')          
    popDictFull['L5_I']= (1065,'L5','IF_curr_exp_L5_I','single')
    popDictFull['L6_E']= (14395,'L23','IF_curr_exp_L6_E','single')
    popDictFull['L6_I']= (2948,'L6','IF_curr_exp_L6_I','single')
    popDictFull['Thalamus']=(thal_params['n_thal'],'Thalamus','Thalamus_Input','single')
    
    pop_ids=['L23_E','L23_I','L4_E','L4_I', 'L5_E','L5_I', 'L6_E','L6_I']
    
    n_layers = 4
    
    n_pops_per_layer = 2
              
    K_full = np.zeros([n_layers * n_pops_per_layer, n_layers * n_pops_per_layer])
    
    #######################################################################################################
    
    nml_doc, network = oc.generate_network(net_id,seed)
    
    popDict={}
    
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
                 
                 thal_tuple=(int(round(scale_thalamus*popDictFull[cell_pop_id][0])), 
                                       popDictFull[cell_pop_id][1],
                                       popDictFull[cell_pop_id][2],
                                       popDictFull[cell_pop_id][3])
                  
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
               
               popDictFinal[new_pop_id]=(1,popDict[cell_pop_id][1],popDict[cell_pop_id][2]+str(cell_ind),popDict[cell_pop_id][3])
            
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
      
       #pop_params=oc_utils.add_populations_in_cylindrical_layers(network,boundaries,popDictFinal,radiusOfCylinder=500,numOfSides=3)
       
       #pop_params=oc_utils.add_populations_in_cylindrical_layers(network,boundaries,popDictFinal,radiusOfCylinder=500)
                                                                 
       pop_params=oc_utils.add_populations_in_rectangular_layers(network,boundaries,popDictFinal,xs,zs) 
       
    else:
    
       opencortex.print_comment_v("Population parameters were specified incorrectly; execution of RunPotjans2014.py will terminate.")
       
       quit() 
    
    # Probabilities for >=1 connection between neurons in the given populations. 
    # The first index is for the target population; the second for the source population
    #             2/3e      2/3i    4e      4i      5e      5i      6e      6i
    #pop_ids=   ['L23_E','L23_I','L4_E','L4_I', 'L5_E','L5_I', 'L6_E','L6_I']
    
    conn_probs = [[0.1009,  0.1689, 0.0437, 0.0818, 0.0323, 0.,     0.0076, 0.    ],
                 [0.1346,   0.1371, 0.0316, 0.0515, 0.0755, 0.,     0.0042, 0.    ],
                 [0.0077,   0.0059, 0.0497, 0.135,  0.0067, 0.0003, 0.0453, 0.    ],
                 [0.0691,   0.0029, 0.0794, 0.1597, 0.0033, 0.,     0.1057, 0.    ],
                 [0.1004,   0.0622, 0.0505, 0.0057, 0.0831, 0.3726, 0.0204, 0.    ],
                 [0.0548,   0.0269, 0.0257, 0.0022, 0.06,   0.3158, 0.0086, 0.    ],
                 [0.0156,   0.0066, 0.0211, 0.0166, 0.0572, 0.0197, 0.0396, 0.2252],
                 [0.0364,   0.001,  0.0034, 0.0005, 0.0277, 0.008,  0.0658, 0.1443]]
                 
    conn_mean_w=[[w_mean,  rel_inh_syn_w*w_mean,   w_234 ,   rel_inh_syn_w*w_mean,  w_mean, rel_inh_syn_w*w_mean, w_mean, rel_inh_syn_w*w_mean],
                 [w_mean,  rel_inh_syn_w*w_mean,   w_mean,   rel_inh_syn_w*w_mean, w_mean, rel_inh_syn_w*w_mean, w_mean, rel_inh_syn_w*w_mean],
                 [w_mean,  rel_inh_syn_w*w_mean,   w_mean,   rel_inh_syn_w*w_mean, w_mean, rel_inh_syn_w*w_mean, w_mean, rel_inh_syn_w*w_mean],
                 [w_mean,  rel_inh_syn_w*w_mean,   w_mean,   rel_inh_syn_w*w_mean, w_mean, rel_inh_syn_w*w_mean, w_mean, rel_inh_syn_w*w_mean],
                 [w_mean,  rel_inh_syn_w*w_mean,   w_mean,   rel_inh_syn_w*w_mean, w_mean, rel_inh_syn_w*w_mean, w_mean, rel_inh_syn_w*w_mean],
                 [w_mean,  rel_inh_syn_w*w_mean,   w_mean,   rel_inh_syn_w*w_mean, w_mean, rel_inh_syn_w*w_mean, w_mean, rel_inh_syn_w*w_mean],
                 [w_mean,  rel_inh_syn_w*w_mean,   w_mean,   rel_inh_syn_w*w_mean, w_mean, rel_inh_syn_w*w_mean, w_mean, rel_inh_syn_w*w_mean],
                 [w_mean,  rel_inh_syn_w*w_mean,   w_mean,   rel_inh_syn_w*w_mean, w_mean, rel_inh_syn_w*w_mean, w_mean, rel_inh_syn_w*w_mean]]  
                
    conn_std_w=[]
                
    for target_pop_index in range(0,len(pop_ids)):
    
        conn_std_w_per_target_pop=[]
    
        for source_pop_index in range(0,len(pop_ids)):
        
            w_val=conn_mean_w[target_pop_index][source_pop_index]
        
            if pop_ids[source_pop_index]=="L4_E" and pop_ids[target_pop_index]=="L23_E":
            
               w_sd=w_val*w_rel_234
            
            else:
            
               w_sd=abs(w_val * w_rel)
               
            conn_std_w_per_target_pop.append(w_sd)
            
        conn_std_w.append(conn_std_w_per_target_pop)
                
    conn_mean_delay=[[d_mean['E'],  d_mean['I'], d_mean['E'], d_mean['I'], d_mean['E'], d_mean['I'], d_mean['E'], d_mean['I']],
                     [d_mean['E'],  d_mean['I'], d_mean['E'], d_mean['I'], d_mean['E'], d_mean['I'], d_mean['E'], d_mean['I']],
                     [d_mean['E'],  d_mean['I'], d_mean['E'], d_mean['I'], d_mean['E'], d_mean['I'], d_mean['E'], d_mean['I']],
                     [d_mean['E'],  d_mean['I'], d_mean['E'], d_mean['I'], d_mean['E'], d_mean['I'], d_mean['E'], d_mean['I']],
                     [d_mean['E'],  d_mean['I'], d_mean['E'], d_mean['I'], d_mean['E'], d_mean['I'], d_mean['E'], d_mean['I']],
                     [d_mean['E'],  d_mean['I'], d_mean['E'], d_mean['I'], d_mean['E'], d_mean['I'], d_mean['E'], d_mean['I']],
                     [d_mean['E'],  d_mean['I'], d_mean['E'], d_mean['I'], d_mean['E'], d_mean['I'], d_mean['E'], d_mean['I']],
                     [d_mean['E'],  d_mean['I'], d_mean['E'], d_mean['I'], d_mean['E'], d_mean['I'], d_mean['E'], d_mean['I']]] 
                         
    conn_std_delay=[[d_sd['E'],  d_sd['I'], d_sd['E'], d_sd['I'], d_sd['E'], d_sd['I'], d_sd['E'], d_sd['I']],
                    [d_sd['E'],  d_sd['I'], d_sd['E'], d_sd['I'], d_sd['E'], d_sd['I'], d_sd['E'], d_sd['I']],
                    [d_sd['E'],  d_sd['I'], d_sd['E'], d_sd['I'], d_sd['E'], d_sd['I'], d_sd['E'], d_sd['I']],
                    [d_sd['E'],  d_sd['I'], d_sd['E'], d_sd['I'], d_sd['E'], d_sd['I'], d_sd['E'], d_sd['I']],
                    [d_sd['E'],  d_sd['I'], d_sd['E'], d_sd['I'], d_sd['E'], d_sd['I'], d_sd['E'], d_sd['I']],
                    [d_sd['E'],  d_sd['I'], d_sd['E'], d_sd['I'], d_sd['E'], d_sd['I'], d_sd['E'], d_sd['I']],
                    [d_sd['E'],  d_sd['I'], d_sd['E'], d_sd['I'], d_sd['E'], d_sd['I'], d_sd['E'], d_sd['I']],
                    [d_sd['E'],  d_sd['I'], d_sd['E'], d_sd['I'], d_sd['E'], d_sd['I'], d_sd['E'], d_sd['I']]] 
                    
    syn=neuroml.ExpCurrSynapse(id='exp_curr_syn_all',tau_syn=0.5)
    
    nml_doc.exp_curr_synapses.append(syn)
                    
    syn_id_matrix=[['exp_curr_syn_all']]       # utils method build_probability_based_connectivity will assume that the same synapse model is shared by all projections; 
                                               # however, it must be inside 'list' because generically each physical projection might contain multiple synaptic components.
                                               
           
    #### get in-degrees for all connections in the full scale model according to scaling.py in the original project
    
    for source_pop in pop_ids:
    
        for target_pop in pop_ids:
        
            n_target = popDictFull[target_pop][0]
            
            n_source = popDictFull[source_pop][0]
            
            K_full[pop_ids.index(target_pop)][pop_ids.index(source_pop)] = round(np.log(1. -
            conn_probs[pop_ids.index(target_pop)][pop_ids.index(source_pop)]) / np.log(
            (n_target * n_source - 1.) / (n_target * n_source))) / n_target
    
    input_params ={'L23_E':[{'InputType':'GenerateSpikeSourcePoisson',
                             'InputName':"EXT_L23_E",
                             'AverageRateList':[],
                             'DurationList':[],
                             'DelayList':[],
                             'WeightList':[],
                             'Synapse':'exp_curr_syn_all',
                             'RateUnits':'Hz',
                             'TimeUnits':'ms',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1} },
                             
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
                             'TargetDict':{None:1}  }],
                     
                   'L23_I':[{'InputType':'GenerateSpikeSourcePoisson',
                             'InputName':"EXT_L23_I",
                             'AverageRateList':[],
                             'DurationList':[],
                             'DelayList':[],
                             'WeightList':[],
                             'Synapse':'exp_curr_syn_all',
                             'RateUnits':'Hz',
                             'TimeUnits':'ms',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1} },
                             
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
                             'TargetDict':{None:1}  }],
                     
                   'L4_E':[ {'InputType':'GenerateSpikeSourcePoisson',
                             'InputName':"EXT_L4_E",
                             'AverageRateList':[],
                             'DurationList':[],
                             'DelayList':[],
                             'WeightList':[],
                             'Synapse':'exp_curr_syn_all',
                             'RateUnits':'Hz',
                             'TimeUnits':'ms',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1} },
                             
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
                             'TargetDict':{None:1}  }], 
                     
                   'L4_I':[ {'InputType':'GenerateSpikeSourcePoisson',
                             'InputName':"EXT_L4_I",
                             'AverageRateList':[],
                             'DurationList':[],
                             'DelayList':[],
                             'WeightList':[],
                             'Synapse':'exp_curr_syn_all',
                             'RateUnits':'Hz',
                             'TimeUnits':'ms',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1}},
                             
                            {'InputType':'PulseGenerators',
                             'InputName':"Ext_L4_I",
                             'Noise':False,
                             'AmplitudeList':[0.0],
                             'DurationList':[0.0],
                             'DelayList':[0.0],
                             'TimeUnits':'ms',
                             'AmplitudeUnits':'nA',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1}  } ],
                     
                   'L5_E':[ {'InputType':'GenerateSpikeSourcePoisson',
                             'InputName':"EXT_L5_E",
                             'AverageRateList':[],
                             'DurationList':[],
                             'DelayList':[],
                             'WeightList':[],
                             'Synapse':'exp_curr_syn_all',
                             'RateUnits':'Hz',
                             'TimeUnits':'ms',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1}  },
                             
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
                             'TargetDict':{None:1}  } ],
                             
                   'L5_I':[ {'InputType':'GenerateSpikeSourcePoisson',
                             'InputName':"EXT_L5_I",
                             'AverageRateList':[],
                             'DurationList':[],
                             'DelayList':[],
                             'WeightList':[],
                             'Synapse':'exp_curr_syn_all',
                             'RateUnits':'Hz',
                             'TimeUnits':'ms',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1} },
                             
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
                             'TargetDict':{None:1}  } ],
                     
                   'L6_E':[ {'InputType':'GenerateSpikeSourcePoisson',
                             'InputName':"EXT_L6_E",
                             'AverageRateList':[],
                             'DurationList':[],
                             'DelayList':[],
                             'WeightList':[],
                             'Synapse':'exp_curr_syn_all',
                             'RateUnits':'Hz',
                             'TimeUnits':'ms',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1} },
                             
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
                             'TargetDict':{None:1}  } ],    
                             
                   'L6_I':[ {'InputType':'GenerateSpikeSourcePoisson',
                             'InputName':"EXT_L6_I",
                             'AverageRateList':[],
                             'DurationList':[],
                             'DelayList':[],
                             'WeightList':[],
                             'Synapse':'exp_curr_syn_all',
                             'RateUnits':'Hz',
                             'TimeUnits':'ms',
                             'FractionToTarget':1.0,
                             'LocationSpecific':False,
                             'TargetDict':{None:1} },
                             
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
                             'TargetDict':{None:1}  } ] }
    
    DC_amp = {}
    
    for target_pop_index in range(0,len(pop_ids)):
    
        if input_type == "DC":
           
           DC_amp[pop_ids[target_pop_index]] = bg_rate *K_ext[pop_ids[target_pop_index]] * w_mean * neuron_params['tau_syn_E'] / 1000.0
           
        else:
       
           DC_amp[pop_ids[target_pop_index]]= 0.0
               
    if K_scaling != 1 :
       
       DC_amp={}     
       
       for target_pop_index in range(0,len(pop_ids)):
           
           input_coefficient = 0
           
           for source_pop_index in range(0,len(pop_ids)):
               
               input_coefficient += conn_mean_w[target_pop_index][source_pop_index] * K_full[target_pop_index][source_pop_index] * full_mean_rates[pop_ids[source_pop_index]]
               
               conn_mean_w[target_pop_index][source_pop_index] = conn_mean_w[target_pop_index][source_pop_index] / np.sqrt(K_scaling)
               
           if input_type=="poisson":
           
              input_coefficient += w_ext*K_ext[pop_ids[target_pop_index]]*bg_rate
              
              K_ext[pop_ids[target_pop_index]] = K_ext[pop_ids[target_pop_index]]*K_scaling
              
           DC_amp[pop_ids[target_pop_index]] = 0.001 * neuron_params['tau_syn_E'] * \
          (1. - np.sqrt(K_scaling)) * input_coefficient + DC[pop_ids[target_pop_index]]
          
       w_ext = w_ext / np.sqrt(K_scaling)
       
    input_params_final={}
              
    for target_pop_tag in input_params.keys(): 
    
        found_target_pop=False
    
        for pop_id in pop_params.keys():
    
            if target_pop_tag  in pop_id:
        
               found_target_pop=True
               
               break
           
        if found_target_pop:
        
           input_params_final[target_pop_tag]=[]
        
           for input_group_ind in range(0,len(input_params[target_pop_tag])):
               
               if (input_type=='DC' or K_scaling !=1) and input_params[target_pop_tag][input_group_ind]['InputType']=='PulseGenerators':
            
                  input_params[target_pop_tag][input_group_ind]['AmplitudeList'].append(DC_amp[target_pop_tag])
                  
                  input_params[target_pop_tag][input_group_ind]['DurationList'].append(0.0)
                  
                  input_params[target_pop_tag][input_group_ind]['DelayList'].append(0.0)
                  
                  input_params_final[target_pop_tag].append(input_params[target_pop_tag][input_group_ind])
            
               if input_type=='poisson' and input_params[target_pop_tag][input_group_ind]['InputType']=='GenerateSpikeSourcePoisson':               
    
                  input_params[target_pop_tag][input_group_ind]['AverageRateList'].append(bg_rate*K_ext[target_pop_tag])
                  
                  input_params[target_pop_tag][input_group_ind]['WeightList'].append(w_ext)
                  
                  input_params[target_pop_tag][input_group_ind]['DurationList'].append(0.0)
                  
                  input_params[target_pop_tag][input_group_ind]['DelayList'].append(0.0)
                  
                  input_params_final[target_pop_tag].append(input_params[target_pop_tag][input_group_ind])
    
    proj_array=oc_utils.build_probability_based_connectivity(net=network,
                                                             pop_params=pop_params,
                                                             probability_matrix=conn_probs, 
                                                             synapse_matrix=syn_id_matrix,
                                                             weight_matrix=conn_mean_w, 
                                                             delay_matrix=conn_mean_delay,
                                                             tags_on_populations=pop_ids, 
                                                             std_weight_matrix=conn_std_w,
                                                             std_delay_matrix=conn_std_delay)
                                                             
    input_list_array_final, input_synapse_list=oc_utils.build_inputs(nml_doc=nml_doc,
                                                                     net=network,
                                                                     population_params=pop_params,
                                                                     input_params=input_params_final,
                                                                     cached_dicts=None,
                                                                     path_to_cells=None,
                                                                     path_to_synapses=None)
                                                                                                                                      
    if thalamic_input:
    
       if thal_tuple[0] != 0:
       
          oc.add_spike_source_poisson(nml_doc, 
                                      id=thal_tuple[2], 
                                      start="%f ms"%thal_params['start'], 
                                      duration="%f ms"%thal_params['duration'], 
                                      rate="%f Hz"%thal_params['rate'])
          
          thalamus_pop = neuroml.Population(id='Thalamus', component=thal_tuple[2], size=thal_tuple[0] )
          
          network.populations.append(thalamus_pop)
          
          for target_pop in thal_params['C'].keys():
          
              oc.add_probabilistic_projection_list(net=network,
                                                   presynaptic_population=thalamus_pop, 
                                                   postsynaptic_population=pop_params[target_pop]['PopObj'], 
                                                   synapse_list=['exp_curr_syn_all'],  
                                                   connection_probability=thal_params['C'][target_pop],
                                                   delay = d_mean['E'],
                                                   weight = w_ext,
                                                   presynaptic_population_list=False,
                                                   std_delay=d_sd['E'],
                                                   std_weight=w_ext*w_rel)
       else:
       
          print("Note: thalamic_input is set to True but population was scaled down to zero, thus thalamic input will not be added.")  
                                                
    nml_file_name = '%s.net.nml'%network.id
    
    oc.save_network(nml_doc, nml_file_name, validate=True,max_memory=max_memory)
    
    lems_file_name=oc.generate_lems_simulation(nml_doc, 
                                               network, 
                                               nml_file_name, 
                                               duration =duration, 
                                               dt =dt,
                                               include_extra_lems_files=["PyNN.xml"],
                                               gen_plots_for_all_v = False,
                                               gen_plots_for_only_populations=pop_params.keys(),
                                               gen_saves_for_all_v = False,
                                               gen_saves_for_only_populations=pop_params.keys() )
    
    if simulator != None:                                          
                                               
       opencortex.print_comment_v("Starting simulation of %s.net.nml"%net_id)
                            
       oc.simulate_network(lems_file_name=lems_file_name,
                           simulator=simulator,
                           max_memory=max_memory)
    
    
if __name__=="__main__":

   ## generation is faster when initial membrane potential does not vary with the cell instance
   RunPotjans2014(V0_mean = None,
                  V0_sd= None,
                  thalamic_input=True,
                  max_memory='8000M',
                  duration=1000,
                  simulator=None)
   
   #RunPotjans2014()
