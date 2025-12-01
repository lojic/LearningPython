from advent import parse, words, cache
import multiprocessing

@cache
def check_design(design, pats):
    if design == '':
        return 1
    else:
        return sum(check_design(design.removeprefix(pat), pats) for pat in pats if design.startswith(pat))

    
#counts = [ cnt for design in designs if (cnt := check_design(design)) > 0 ]

#assert len(counts) == 353             # Part 1
#assert sum(counts) == 880877787214477 # Part 2

def main():
    pats, designs = parse(19, words, sep='\n\n')
    num_cores = multiprocessing.cpu_count()
    print(f'Using {num_cores} cores')

    with multiprocessing.Pool(processes=num_cores) as pool:
        counts = pool.map(check_design, [(design, pats) for design in designs ])

    assert sum(counts) == 880877787214477 # Part 2

if __name__ == "__main__":
    main()
