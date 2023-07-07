import torch
import pytest
from GeneSplice.model import GeneSplice, GeneSpliceTokenizer  # Assuming the module name is GeneSplice

def test_tokenizer_initialization():
    tokenizer = GeneSpliceTokenizer()
    assert tokenizer is not None, "Tokenizer failed to initialize"

def test_model_initialization():
    model = GeneSplice()
    assert model is not None, "Model failed to initialize"

def test_tokenization():
    tokenizer = GeneSpliceTokenizer()
    text = "Hello, world!"
    tokens = tokenizer.tokenize_texts(text)
    assert tokens is not None, "Tokenization failed"
    assert tokens.shape[1] > 0, "Tokenization resulted in zero tokens"

def test_model_forward():
    model = GeneSplice()
    tokenizer = GeneSpliceTokenizer()
    text = "Hello, world!"
    tokens = tokenizer.tokenize_texts(text)
    output = model(tokens)
    assert output is not None, "Forward pass failed"
    assert output.shape == tokens.shape, "Output shape is different from input shape"

if __name__ == "__main__":
    pytest.main()
