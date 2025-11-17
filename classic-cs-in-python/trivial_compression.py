class CompressedGene:
    def __init__(self, gene: str) -> None:
        """Assumes gene contains only 'A', 'C', 'G' or 'T'"""
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1  # Sentinel

        for nucleotide in gene:
            self.bit_string <<= 2

            match nucleotide:
                case 'A':
                    pass  # No need to do anything to get 0b00 after <<
                case 'C':
                    self.bit_string |= 0b01
                case 'G':
                    self.bit_string |= 0b10
                case 'T':
                    self.bit_string |= 0b11
                case _:
                    raise ValueError(f'Invalid Nucleotide: {nucleotide}')

    def decompress(self) -> str:
        gene: list[str] = []

        for i in range(0, self.bit_string.bit_length() - 1, 2):  # -1 to exclude sentinel
            bits: int = self.bit_string >> i & 0b11

            match bits:
                case 0b00:
                    gene.append('A')
                case 0b01:
                    gene.append('C')
                case 0b10:
                    gene.append('G')
                case 0b11:
                    gene.append('T')
                case _:
                    raise ValueError(f'Invalid bits: {bits}')

        gene.reverse()

        return ''.join(gene)

    def __str__(self) -> str:
        return self.decompress()


if __name__ == '__main__':
    from sys import getsizeof

    # original: str = 'TAGGGAATTACCGTGTGTTGGGCCAAACGT' * 1000
    original: str = 'TAGCATCGAT'
    print(f'original is {getsizeof(original)} bytes')
    compressed: CompressedGene = CompressedGene(original)
    print(f'bit representation is {compressed.bit_string}')

    # NOTE: re: getsizeof()
    # "Only the memory consumption directly attributed to the object is accounted for,
    # not the memory consumption of objects it refers to."
    print(f'compressed is {getsizeof(compressed) + getsizeof(compressed.bit_string)} bytes')

    if original == str(compressed):
        print('original and decompressed are identical')
    else:
        raise RuntimeError('original differs from decompressed')
