
def normalize(scores: list):
    if scores==None:
        return scores
    if len(scores)==0:
        return []    
    _max = max(scores)
    _min = min(scores)
    result = [round(i*_min/_max,1) for i in scores]
    return result
