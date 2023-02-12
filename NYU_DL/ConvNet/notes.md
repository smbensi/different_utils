in signals there a 3 important feature:

- **stationarity** (we can see the same pattern appearing at different locations)
- **locality** (in a region the values of the samples are close)
- **compositionality** (the overall signal represent one things composed of different details)

locality ==> sparsity:
- reduce the amount of computation


stationarity ==> parameter sharing:
- faster convergence
- better generalization ( doesnt specific to a region)
- not constrained to input size
- kernel independence => high parallelization

### kernel size:

**For 1D signal**: C_out x C_in x h

### zero padding

(h-1)/2

# RNN

handling sequential data