import wikipedia

def get_object_info(object_name):

    try:
        summary = wikipedia.summary(object_name, sentences=2)
        return summary

    except:
        return "No information found for this object."