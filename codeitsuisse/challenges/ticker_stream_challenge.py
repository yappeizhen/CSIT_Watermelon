def to_cumulative_helper(stream: list, isNotionalCalculated: bool):
    timemap = {}  # Maps timestamp to ticker data
    for obj in stream:
        # ===== Data Extraction =====
        item = obj.split(",")
        timestamp = item[0]
        ticker = item[1]
        quantity = item[2]
        price = item[3]
        # ===== Populate Data Structures =====
        if timestamp in timemap:
            # Get the existing ticker map for updating
            tickermap = timemap[timestamp]
            cur_ticker = {
                'cum_quantity': 0,
                'cum_notional': 0
            }
            if ticker in tickermap:
                cur_ticker = tickermap[ticker]
            # Update aggregated values for this ticker
            cur_ticker['cum_quantity'] += int(quantity)
            notional_val = float(price)
            if isNotionalCalculated == False:
                notional_val = float(price) * float(quantity)
            cur_ticker['cum_notional'] += notional_val
            # Save changes to tickermap
            tickermap[ticker] = cur_ticker
        else:
            # Create a new tickermap to store the new entry
            notional_val = float(price)
            if isNotionalCalculated == False:
                notional_val = float(price) * float(quantity)
            new_ticker_entry = {
                'cum_quantity': int(quantity),
                'cum_notional': notional_val
            }
            new_tickermap = {}
            new_tickermap[ticker] = new_ticker_entry
            # Update timemap
            timemap[timestamp] = new_tickermap
    # ===== Result Processing =====
    result = []  # List of strings
    # Get a sorted list of timestamp values in timemap
    timestamp_keyset = list(timemap.keys())
    timestamp_keyset.sort()
    for ts in timestamp_keyset:
        tickermap = timemap[ts]
        timestamp_datastring = ts + ','
        # Get a sorted list of tickers
        ticker_keyset = list(tickermap.keys())
        ticker_keyset.sort()
        for ticker_id in ticker_keyset:
            cum_quant = tickermap[ticker_id]['cum_quantity']
            cum_notion = tickermap[ticker_id]['cum_notional']
            timestamp_datastring += ticker_id + ',' + \
                str(cum_quant) + ',' + str(round(cum_notion, 1)) + ','
        result.append(timestamp_datastring[:-1])
    return result

def to_cumulative(stream: list):
    return to_cumulative_helper(stream, False)
    

def to_cumulative_delayed(stream: list, quantity_block: int):
    tickermap = {}  # Maps timestamps to ticker data
    for obj in stream:
        # ===== Data Extraction =====
        item = obj.split(",")
        timestamp = item[0]
        ticker = item[1]
        quantity = item[2]
        price = item[3]
        # ===== Populate Data Structures =====
        if ticker in tickermap:
            # Get the existing timestamp map for updating
            timemap = tickermap[ticker]
            cur_timestamp = {
                'cum_quantity': 0,
                'price': 0
            }
            if timestamp in timemap:
                cur_timestamp = timemap[timestamp]
            # Update aggregated values for this timestamp
            cur_timestamp['cum_quantity'] += int(quantity)
            cur_timestamp['price'] = float(price)
            # Save changes to timemap
            timemap[timestamp] = cur_timestamp
        else:
            # Create a new timemap to store the new entry
            new_time_entry = {
                'cum_quantity': int(quantity),
                'price': float(price)
            }
            new_timemap = {}
            new_timemap[timestamp] = new_time_entry
            # Update tickermap
            tickermap[ticker] = new_timemap
    # ===== Data Processing =====
    result = []  # List of strings
    # Get a sorted list of ticker values in tickermap
    ticker_keyset = list(tickermap.keys())
    ticker_keyset.sort()
    for tick in ticker_keyset:
        cur_qty = 0
        cur_notion = 0.0
        cur_ts = "00:00"
        timemap = tickermap[tick]
        # Get a sorted list of timestamps
        time_keyset = list(timemap.keys())
        time_keyset.sort()
        if len(time_keyset) > 0:
          cur_ts = time_keyset[0]
        for ts in time_keyset:
            qty_to_add = quantity_block - cur_qty
            qty_to_add = min(qty_to_add, timemap[ts]['cum_quantity'])
            if (qty_to_add == 0):
                break
            cur_qty += qty_to_add
            cur_notion += timemap[ts]['price'] * float(qty_to_add)
            cur_ts = ts
        print(cur_ts, tick, cur_qty, cur_notion)
        ticker_datastring = cur_ts + ',' + tick + ',' + \
            str(cur_qty) + ',' + str(round(cur_notion, 1))
        result.append(ticker_datastring)
    # ===== Result Formatting =====
    # Aggregate all entries of the same timestamp
    formatted_result = to_cumulative_helper(result, True)
    formatted_result.sort()
    return formatted_result
