import altair as alt
import pandas as pd
from altair_saver import save

#fname='aes_cf.angr'

# import raw perf csv file
def get_perf_stats(filename):
    data = pd.read_csv(filename, sep=',', usecols=[0,1,3,6,7], names=['time','val1','key1','val2','key2'], skiprows=range(0,2))
    #data = data.drop(labels=1, axis=1)
    return data

'''
   time        val1                         key1    val2             key2 
   0   0.400235  1150001454                 cycles   NaN             NaN 
   1   0.400235  1589611615           instructions  1.38  insn per cycle 
   2   0.400235     6997434          branch-misses   NaN             NaN 
   3   0.400235    26199795  L1-dcache-load-misses   NaN             NaN 
   4   0.400235     6784876          l2_rqsts.miss   NaN             NaN 
   5   0.800518  1170270707                 cycles   NaN             NaN
'''
def get_metric(state, metric):
    keys = {
            1: 'time',
            2: 'val2', # IPC
            3: 'val1', # branch-misses
            4: 'val1', # L1 d$ ld miss
            5: 'val1' # L2 $ misses
    }
    value = metric[keys[state]]
    return value

def record_metric(state, metric, records, insts):
    keys = {
            1: 'x_exec',
            2: 'ipc_y', # IPC
            3: 'bp_miss_y', # branch-misses
            4: 'l1_miss_y', # L1 d$ ld miss
            5: 'l2_miss_y' # L2 $ misses
    }
    if(state > 2):
        # print("{} {} {} {}".format(type(metric),metric, type(insts), insts))
        try:
            m = int(metric) / int(insts)
        except:
            m = 0
    else:
        m = metric
    record_key = keys[state]
    records[record_key].append(m)
    pass

def graph_data(fname):
    # iterate through all file names
    df = get_perf_stats(fname)

    #print(df)

    # iterate through whole csv
    count = 0
    insts = 0
    records = {
            'x_exec': [],
            'ipc_y': [],
            'bp_miss_y': [],
            'l1_miss_y': [],
            'l2_miss_y': []
    }
    
    for index, metric in df.iterrows():
        count += 1
        # collect sample
        m = get_metric(count, metric)
        if(count == 2):
            insts = metric['val1']
        # add them to the appropriate "list"
        record_metric(count, m, records, insts)
        # reset state on what to record
        if (count % 5 == 0):
            count = 0

    return records

if __name__ == '__main__':
    # iterate through all logic bombs
    TOOLS = ['mcore']#, 'mcore']
    LOGIC_BOMBS = ['2thread_pp_l1','df2cf_cp_l1','float5_fp_l2','pid_csv','stack_bo_l1','2thread_pp_l2','echo_cp_l1',
            'forkpipe_pp_l1','ping_csv','stack_bo_l2','5n+1_lo_l1','echofile_cp_l1','forkshm_pp_l1','pointers_sj_l1',
            'stack_cp_l1','7n+1_lo_l1','file_cp_l1','heap_bo_l1','pow_ef_l2','stackarray_sm_l1','addint_to_l1',
            'file_csv','heapoutofbound_sm_l2','printfloat_ef_l1','stackarray_sm_l2','aes_cf','file_posix_cp_l1','jmp_sj_l1',
            'printint_int_l1','stackarray_sm_ln','arrayjmp_sj_l2','file_posix_csv','ln_ef_l2','rand_ef_l2','stacknocrash_bo_l1',
            'atof_ef_l2','float1_fp_l1','malloc_sm_l1','realloc_sm_l1','stackoutofbound_sm_l2','atoi_ef_l2','float2_fp_l1',
            'mthread_pp_l2','sha_cf','syscall_csv', 'collaz_lo_l1', 'float3_fp_l2', 'multiplyint_to_l1', 'sin_ef_l2',
            'collaz_lo_l2','float4_fp_l2','paraloop_lo_l2','socket_cp_l1']
    
    results = {}
    for bomb in LOGIC_BOMBS:
        entry = []
        for tool in TOOLS:
            # print(bomb)
            # "graph" data for this tool
            entry.append(graph_data(bomb+'.'+tool))
        # save data in dictionary for later
        results[bomb] = entry
        
    # create Execution Time Plot
    for x in range(len(TOOLS)):
        # create simple bar graph
        source = pd.DataFrame({
            'Logic Bomb':LOGIC_BOMBS,
            'Execution Time (seconds)':[ results[bomb][x]['x_exec'][-1] 
                for bomb in LOGIC_BOMBS ]
        })

        plot = alt.Chart(source).mark_bar().encode(
            x='Logic Bomb',
            y='Execution Time (seconds)'
            ).properties(title=TOOLS[x]+' Execution Times')
        save(plot, TOOLS[x]+'-exec.png')

'''
    lb = fname.split('.')
    # create simple bar graph
    source = pd.DataFrame({
        'Logic Bomb':[LOGIC_BOMBS],
        'Execution Time (seconds)':[ results[bomb][0]['x_exec'][-1] for bomb in LOGIC_BOMBS ]
        })

    plot = alt.Chart(source).mark_bar().encode(
        x='Logic Bomb',
        y='Execution Time (seconds)'
        ).properties(title='angr Execution Times')
    save(plot, 'angr-exec.png')
'''



# graph_data()
