import os

def process_data(data_path=None, input_data=None):
    """
    Convenience method to read from a data set

    Args:
        input_data (list, optional): Defaults to None. Series of positive and negative integers

    Returns:
        list: Series of positive and negative integers
    """

    if input_data is None:
        if os.path.exists(data_path):
            with open(data_path) as fp:
                input_data = []
                for line in fp.read().split('\n'):
                    if line:
                        try:
                            line = int(line)
                        except:
                            pass

                        input_data.append(line)
        else:
            print 'Path does not exist: {0}'.format(data_path)
    return input_data
