[NEURAL MACHINE TRANSLATION
BY JOINTLY LEARNING TO ALIGN AND TRANSLATE](https://arxiv.org/pdf/1409.0473.pdf)

- problem with the encoder-decoder arch because encoded in a fixed-length vector and it's a **bottleneck**
- **proposition**: allowing a model to automatically (soft-)search for parts of a source sentence that are relevant to predicting a target word.
- neural machine translation attempts to build and train a single, large NN that reads a sentence and outputs a correct translation.
- thee encoder and the decoder for a language pair, is jointly trained to maximize the proba of a correct translation given a source sentence.
- **proposition**: extension to the encoder-decoder model which learns to align and translate jointly. Each time the proposed model generates a word in a translation, it (soft-)searches for a set of positions in a source sentence where the most relevant info is concentrated. The model then predicts a target word based on the context vectors associated with these source positions and all the previous generated target words.
- It encodes the input sequence into a sequence of vectors and choose a subset of these vectors adaptively while decoding the translation.
- the proposed model finds a linguistically plausible (soft-)alignment between a source sentence and the corresponding target sentence.
  

## Background

- From a probabilistic perspective, translation is equivalent to finding a target sentence **y** that maximizes the conditional proba of **y** given a source sentence **x**, i.e *argmax_y p(y|x)* 
  
### RNN Encoder-Decoder

In the Encoder-Decoder framework, an encoder reads the input sentence, a sequence of vectors **x**=(x_1, ... , x_Tx), into a vector *c*. The most common approach is to use an RNN such that   *h_t = f(x_t, h_(t-1))* and *c = q({h_1, ..., h_Tx})*
*c* is a vector generated from the sequence of the hidden states. f and q are nonlinear functions.

The decoder is often trained to predict the next word *y_t* given the context vector *c* and all the previously predicted words *{y_1,...,y_(t-1)}*. In other words, the decoder defines a probability over the translation **y** by decomposing the joint probability into the ordered conditionals:

p(y) = prod(t=1,T; p(y_t | {y_1,...,y_(t-1)},c)). 

With an RNN, each conditional proba is modeled as

p(y_t | {y_1,...,y_(t-1)},c) = g(y_t-1, s_t, c)

where g is a nonlinear function that outputs the proba of y_t, and s_t is the hidden state of the RNN

## Learning to Align and Translate

- The new architecture consists of a bidirectional RNN as an encoder and a decoder that emulated searching through a source sentence during decoding translation

### Decoder : general description

we define each conditional proba as 

p(y_i | y_1,...,y_(i-1),**x**) = g(y_(i-1), s_i, **c_i**)

where s_i is an RNN hidden state for time i computed by s_i = f(s_i-1, y_i-1, **c_i**)

unlike the existing encoder-decoder approach, here the proba is conditioned on a distinct context vector *c_i* for each target word *y_i*

The context vector *c_i* depends on a sequence of *annotations* (h_1,...,h_Tx) to which an encoder maps the input sequence. Each annotation *h_i* contains info about the whole input sequence with a strong focus on the parts surrounding the i-th word of the input sequence.

The context vector *c_i* is ,then, computed as a weighted sum of these annotations h_i:

c_i = sum(j=1,T_x ; alpha_ij*h_j) the weight alpha_ij of each annotation h_j is computed by :
alpha_ij = (exp(e_ij)/ sum(k=1,T_x ; exp(e_ik)))

where e_ij = a(s_i-1, h_j) is an **alignment model** which scores how well the inputs around position j and the output at position i match. The score is based on the RNN hidden state s_(i-1) and the j-th annotation h_j of the input sequence.

We parametrize the alignment model *a* as a feedforward NN which is jointly trained with all the other components of the proposed system