def create_codon_dict(file_path):
  path = file_path
  file = open(path, "r")
  rows = file.readlines()
  file.close()

  codon_to_amino_dict = {}
  for r in rows:
    cells = r.strip().split('\t')
    codon_to_amino_dict[cells[0]] = cells[2]
  return codon_to_amino_dict


