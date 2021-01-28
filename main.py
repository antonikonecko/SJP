import random

class RandomSeq:
  def __init__(self, sequence_length):
      self.sequence_length = sequence_length

  def __iter__(self):
    self.index = 0
    return self

  def __next__(self):
    if self.index >= self.sequence_length:
      raise StopIteration
    self.index += 1
    return random.choice('ATCG')

if __name__ == '__main__':

    def to_complementary(org_sequence):
        d = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        complementary_sequence = ""
        for char in org_sequence:
            complementary_sequence += d[char]
        return complementary_sequence

    import argparse
    desc = f'Generate random DNA sequence of given length and complementary sequence.'
    p = argparse.ArgumentParser(description=desc)
    p.add_argument('-length', dest='sequence_length', type=int, default=20,
                   metavar="<int>", help='Number of nucleotides [default = %(default)s]')

    p.add_argument('--out', dest='output', type=argparse.FileType('w'),
                   default="sequences.txt", metavar="<file>",
                   help='Output file name [default = %(default)s]')
    args = p.parse_args()
    random_sequence: str = ''.join(RandomSeq(args.sequence_length))
    print(f'____________________________________________________________________________\n{desc}\n____________________________________________________________________________')
    print(f'>Original Sequence:      {random_sequence}\n>Complementary Sequence: {to_complementary(random_sequence)}\n')
    print(f'Output file saved as: {args.output.name}')
    args.output.write(f'>Original Sequence:      {random_sequence}\n>Complementary Sequence: {to_complementary(random_sequence)}\n')
    args.output.close()