from advent import parse, partition, cross_product

pairs = [ (schematic[0][0] == '#', [ len(partition(line, lambda c: c == line[0])[0])
                                     for line in schematic ])
          for schematic in parse(25, lambda s: list(zip(*str.split(s, '\n'))), sep='\n\n') ]
locks = [ lengths for is_lock, lengths in pairs if is_lock     ]
keys  = [ lengths for is_lock, lengths in pairs if not is_lock ]
pins  = 5
total = sum(1 for lock, key in cross_product(locks, keys) if all([ lock[pin] <= key[pin]
                                                                   for pin in range(pins) ]))

assert total == 2618
