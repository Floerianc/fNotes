import configparser

def readConfig():
    config = configparser.ConfigParser()
    
    config.read('user_content/config.ini')
    
    try:
        language = int(config.get('Settings', 'language'))
        decimalNumbers = int(config.get('Settings', 'dec'))
        autoSave = int(config.get('Settings', 'autoSave'))
        wrap = int(config.get('Settings', 'wrap'))
        fontsize = int(config.get('Settings', 'fontsize'))
    
    except Exception as e:
        raise ValueError(f"Couldn't read one or more values from config.\n{e}")
    
    finishedConfig = {
        'language': language,
        'decimalNumbers': decimalNumbers,
        'autoSave': autoSave,
        'wrap': wrap,
        'fontsize': fontsize
    }
    
    return finishedConfig

def writeConfig(settings):
    config = configparser.ConfigParser()
    
    config['Settings'] = {
        'language': settings['lang'],
        'dec': settings['dec'],
        'autoSave': settings['auto'],
        'wrap': settings['wrap'],
        'fontsize': settings['fontsize']
    }
    
    with open('user_content/config.ini', "w") as configfile:
        config.write(configfile)