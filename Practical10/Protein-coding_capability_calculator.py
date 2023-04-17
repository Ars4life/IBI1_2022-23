def Procoding_cap_cal(seq):
    seq_treated = str(seq).upper()
    total_len = len(seq_treated)
    start_point = seq_treated.find('ATG')
    end_point = seq_treated.find('TGA')
    coding_len = end_point - start_point
    percentage = coding_len/total_len
    if percentage > 0.5:
        return '%.2f%%' % (percentage * 100), 'protein-coding'
    elif percentage < 0.1:
        return '%.2f%%' % (percentage * 100), 'non-coding'
    else:
        return unclear
