# RESERVED TOKENS
# NOTE: vocab size is len(reversed) + len(vocab)
PADDING_INDEX = 0
UNKNOWN_INDEX = 1
EOS_INDEX = 2
SOS_INDEX = 3
COPY_INDEX = 4
PADDING_TOKEN = '<pad>'
UNKNOWN_TOKEN = '<unk>'
EOS_TOKEN = '<eos>'
SOS_TOKEN = '<sos>'
COPY_TOKEN = '<copy>'
RESERVED_ITOS = [PADDING_TOKEN, UNKNOWN_TOKEN, EOS_TOKEN, SOS_TOKEN, COPY_TOKEN]
RESERVED_STOI = {token: index for index, token in enumerate(RESERVED_ITOS)}