def to_cumulative(stream: list):
    """Return Cumulative

    Args:
        stream (list): list of string containing streams

    Returns:
        _type_: list of string containing cumulative delayed
    """
    stream.sort() # sort stream list
    timeDict = {} # hashmap to store timestamps
    for cur_stream in stream:
        vars = cur_stream.split(",")
        timeStamp, ticker, quantity, price = (vars[0], vars[1], int(vars[2]),
                                              round(float(vars[3]),1))
        if timeStamp in timeDict:
            # if ticker in timeDict, cumulative sum
            if ticker in timeDict[timeStamp]:
                timeDict[timeStamp][ticker][0] += quantity
                timeDict[timeStamp][ticker][1] += quantity * price
            # if ticker not in timeDict, add ticker to timeDict
            else:
                timeDict[timeStamp][ticker] = [quantity, quantity * price] # add cur_stream to timeDict

        else: # if timeStamp not in timeDict
            timeDict[timeStamp] = {ticker: [quantity, quantity * price]} # initialize timeDict

    # convert timeDict to list of string format
    result = []
    for timeStamp, ticker_group in timeDict.items():
        # append each unique timeStamp to result dict
        timeStampString = f"{timeStamp}"
        for ticker, values in ticker_group.items():
            timeStampString += f",{ticker},{values[0]},{round(values[1],1)}"
        result.append(timeStampString)
    return result


def to_cumulative_delayed(stream: list, quantity_block: int):
    """Return Cumulative Delayed

    Args:
        stream (list): list of string containing streams
        quantity_block (int): cumulative quantity block

    Returns:
        result (list): list of string containing cumulative delayed
    """
    stream.sort()  # sort stream list as stream may not be in chronological order
    runningDict = {} # store most recent running results of cumulative delayed for each corresponding ticker
    resultDict = {} # store most recent results of cumulative delayed for each corresponding ticker where quantity is a multiple of quantity block is reached

    def interative_cumulation_and_check_qty_block(runningDict, resultDict, ticker, quantity, price, quantity_block):
        """Helper function to interative accumulate quantity and notional value of ticker, and updates resultDict if quantity block is reached.

        Args:
            runningDict (dict): runningDict to contain running quantity and notional value for each corresponding ticker
            resultDict (dict): resultDict to contain most recent quantity and notional value for each corresponding ticker where quantity is a multiple of quantity block
            ticker (string): ticker name
            quantity (int): quantity of ticker
            price (float): price of ticker
            quantity_block (int): quantity block
        """
        for i in range(quantity):
            runningDict[ticker][1] += 1
            runningDict[ticker][2] += price
            # check if ticker has cumulative quantity of multiple of quantity block 
            if runningDict[ticker][1] % quantity_block == 0 and runningDict[ticker][1] != 1:
                resultDict[ticker] = runningDict[ticker].copy()

    for cur_stream in stream:
        vars = cur_stream.split(",")
        timeStamp, ticker, quantity, price = (vars[0], vars[1], int(vars[2]),
                                              round(float(vars[3]),1))
        # if ticker in runningDict
        if ticker in runningDict:           
            # cumulative sum
            runningDict[ticker][0] = timeStamp
            interative_cumulation_and_check_qty_block(runningDict, resultDict, ticker, quantity, price, quantity_block)

        else: # if timeStamp not in timeDict, initialize timeDict
            runningDict[ticker] = [timeStamp, 0, 0]
            interative_cumulation_and_check_qty_block(runningDict, resultDict, ticker, quantity, price, quantity_block)

    # Convert resultDict to timeStampDict
    timeStampDict = {}
    for ticker, ticker_group in resultDict.items():
        timeStamp, quantity, notional = ticker_group[0], ticker_group[1], ticker_group[2]
        if timeStamp in timeStampDict:
            timeStampDict[timeStamp].append([ticker, quantity, notional])
        else:
            timeStampDict[timeStamp] = [[ticker, quantity, notional]]

    # convert timeStampDict to list of string format
    result = []
    for timeStamp, ticker_group in timeStampDict.items():
        # append each unique timeStamp to result list
        timeStampString = f"{timeStamp}"
        for values in ticker_group:
            timeStampString += f",{values[0]},{values[1]},{round(values[2],1)}"
        result.append(timeStampString)

    return result