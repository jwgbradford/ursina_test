from json import load

def load_kwargs(file) -> dict:
    with open(file) as input_file:
        dict_data = load(input_file)
    if "scale" in dict_data.keys():
        dict_data = string_to_int(dict_data, "scale")
    elif "position" in dict_data.keys():
        dict_data = string_to_tuple(dict_data, "position")
    return dict_data

def string_to_int(data_dict, key_to_convert) -> dict:
    data_dict[key_to_convert] = int(data_dict[key_to_convert])
    return data_dict

def string_to_tuple(data_dict, key_to_convert) -> dict:
    tup_string = data_dict[key_to_convert]
    tup_tup = ()
    for i in range(len(tup_string)):
        try: 
            int(tup_string[i])
            tup_tup = tup_tup + (int(tup_string[i]),)
        except:
            pass
    data_dict[key_to_convert] = tup_tup
    return data_dict
