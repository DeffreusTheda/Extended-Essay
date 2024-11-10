import re
import sys

def parse_config_h(config_text):
    """
    Parse the config.h file to extract required configuration values.
    
    Args:
        config_text (str): Content of config.h file
        
    Returns:
        dict: Configuration values
    """
    values = {
        'VARIANT': None,
        'CACHE': None,
        'BITS': None,
        'ITERATIONS': None,
        'VICTIM_CALLS': None,
        'TRAINING': None
    }
    
    # Define mapping for CACHE values
    cache_map = {
        "EVICTION": "Eviction",
        "FLUSHING": "Flushing"
    }
    
    # Parse each #define line
    for line in config_text.split('\n'):
        if line.strip().startswith('#define'):
            parts = line.split()
            if len(parts) >= 3:
                key = parts[1]
                value = parts[2]
                
                if key in values:
                    if key == 'CACHE':
                        values[key] = cache_map.get(value)
                    elif key == 'VARIANT':
                        values[key] = 'Spectre-V' + value
                    else:
                        values[key] = value
    
    # Verify all values were found
    if None in values.values():
        missing_fields = [k for k, v in values.items() if v is None]
        return None
    
    return values

def parse_dep(log_text):
    """
    Parse Spectre variant 1 log output and extract specific metrics.
    
    Args:
        log_text (str): The log text to parse
        
    Returns:
        dict: Log values
    """
    values = {
        'miss': None,
        'hit': None,
        'threshold': None,
        'leak_ms': None,
        'bytes_per_sec': None,
        'correct_bits': None,
        'correct_percentage': None,
        'setup_ms': None
    }
    
    # Parse miss, hit, threshold line
    metrics_match = re.search(r'miss: (\d+), hit: (\d+), threshold: (\d+)', log_text)
    if metrics_match:
        values['miss'] = int(metrics_match.group(1))
        values['hit'] = int(metrics_match.group(2))
        values['threshold'] = int(metrics_match.group(3))
    
    # Parse leak statistics line
    leak_match = re.search(r'leaked \d+ byte in (\d+) ms\. \((\d+\.\d+) bytes/s\) correct: (\d+) / \d+ bits \((\d+\.\d+) %\)', log_text)
    if leak_match:
        values['leak_ms'] = int(leak_match.group(1))
        values['bytes_per_sec'] = float(leak_match.group(2))
        values['correct_bits'] = int(leak_match.group(3))
        values['correct_percentage'] = float(leak_match.group(4))
    
    # Parse setup time
    setup_match = re.search(r'setup took: (\d+) ms\.', log_text)
    if setup_match:
        values['setup_ms'] = int(setup_match.group(1))
    
    # Verify all values were found
    if None in values.values():
        missing_fields = [k for k, v in values.items() if v is None]
        raise ValueError(f"Failed to parse all required fields from log. Missing: {missing_fields}")
    
    return values

def parse_ind(sign):
    C = {
        "VARIANT": {
            '1': 'Spectre-V1',
            '2': 'Spectre-V2'
        },
        "CACHE": {
            '0': 'Eviction',
            '1': 'Flushing'
        }
    }

    data = sign.split('-')
    data[-1] = data[-1][:-1] # rm \n
    result = {
        'VARIANT': None,
        'CACHE': None,
        'BITS': None,
        'ITERATIONS': None,
        'VICTIM_CALLS': None,
        'TRAINING': None
    }
    for idx, key in enumerate(result):
        try:
            result[key] = C[key][data[idx]]
        except:
            result[key] = data[idx]

    return result
    

def combine_and_format(ind, dep):
    """
    Combine independent and dependant values into a csv format
    """
    return (f"{ind['VARIANT']}	{ind['CACHE']}	Counter Thread	{ind['BITS']}	"
            f"{ind['ITERATIONS']}	{ind['VICTIM_CALLS']}	{ind['TRAINING']}	"
            f"{dep['miss']}	{dep['hit']}	{dep['threshold']}	{dep['leak_ms']}	"
            f"{dep['bytes_per_sec']:.2f}	{dep['correct_bits']}	{dep['correct_percentage']:.2f}	"
            f"{dep['setup_ms']}")

if __name__ == "__main__":
    # with open('config.h', 'r') as f:
        # config_text = f.read()
    
    dep = ''
    for line in sys.stdin:
        if line[0].isdigit():
            try:
                # config_values = parse_config_h(config_text)
                dep = parse_dep(dep)
                ind = parse_ind(line)
                result = combine_and_format(ind, dep)
                print(result)
            except (ValueError, FileNotFoundError) as e:
                print(f"Error: {e}")
            dep = ''
            continue
        dep += line
